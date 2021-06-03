from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from trade_platform import rest_api
from trade_platform.basic_model import BasicModel
from trade_platform.models import User
from trade_platform.serializers import UserSerializer
from trade_platform.services.profile_service import ProfileService
from trade_platform.services.user_service import UserService
from trade_platform.services.watchlist_service import WatchListService


class UserView(Resource):
    @staticmethod
    @rest_api.route('/register', methods=['POST'])
    def register():
        """
        Endpoint to register new trade_platform
        ---
        parameters:
          - name: email
            in: path
            type: string
            required: true
          - name: username
            in: path
            type: string
            required: true
          - name: password
            in: path
            type: string
            required: true
        """
        serialized = UserSerializer.parse_obj(request.json).dict()
        if UserService.is_unique(serialized['email']):
            user = User(**serialized).insert()
            WatchListService.watchlist_autocreate(ProfileService.profile_autocreate(user))
        else:
            serialized = {"error":"User with this credentials already exists"}

        return jsonify(serialized), 201

    @staticmethod
    @rest_api.route('/user', methods=['GET'])
    @jwt_required()
    def show_users():
        """
        Endpoint to get all users
        ---
        parameters:
          - name: access_token
            required: true
        """
        serialized = [UserSerializer.from_orm(user).dict() for user in User.query.all()]

        return jsonify(serialized), 200

    @staticmethod
    @rest_api.route('/user/<int:id>/', methods=['DELETE'])
    @jwt_required()
    def delete_user(id):
        """
        Endpoint to delete user
        ---
        parameters:
          - name: id
            required: true
        """
        User.query.get(id).delete()
        return jsonify(), 204


    @staticmethod
    @rest_api.route('/user/<int:id>/', methods=['PATCH'])
    @jwt_required()
    def update_user(id):
        """
        Endpoint to edit user's data
        ---
        parameters:
          - name: id
            in: path
            type: int
            required: true
          - name: email
            in: path
            type: string
            required: false
          - name: username
            in: path
            type: string
            required: false
          - name: password
            in: path
            type: string
            required: false
        """
        user = User.query.filter_by(id=id)
        user.update(request.json)
        serialized = UserSerializer.from_orm(user.one()).dict()
        BasicModel.update()

        return jsonify(serialized), 200

    @staticmethod
    @rest_api.route('/get_token', methods=['POST'])
    def login():
        """
        Endpoint to get access_token
        ---
        parameters:
          - name: email
            in: path
            type: string
            required: true
          - name: password
            in: path
            type: string
            required: true
        """
        token = User.authenticate(**request.json).get_token()

        return jsonify({'access_token':token}), 200