from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app import db
from trade_platform import rest_api
from flask import request, jsonify

from trade_platform.models import User
from trade_platform.serializers import UserSerializer


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
        data = request.json
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return jsonify({'username': data['username']}), 201

    @staticmethod
    @rest_api.route('/user', methods=['GET'])
    @jwt_required()
    def show_users():
        """
        Endpoint to show all users
        ---
        parameters:
          - name: access_token
        """
        serialized = [UserSerializer.from_orm(user).dict() for user in User.query.all()]
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
        data = request.json
        user = User.authenticate(**data)
        print(user)
        token = user.get_token()
        return {'access_token':token}
