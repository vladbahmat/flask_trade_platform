from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from trade_platform import rest_api
from flask import request, jsonify

from trade_platform.models import User, Currency, Profile, Item
from trade_platform.serializers import (UserSerializer, CurrencySerializer, CurrencyRetrieveSerializer,
                                        ProfileSerializer, ItemSerializer)
from trade_platform.services.user_service import UserService
from trade_platform.services.profile_service import ProfileService
from trade_platform.services.watchlist_service import WatchListService
from trade_platform.basic_model import BasicModel


class WatchListView(Resource):
    @staticmethod
    @rest_api.route('/item', methods=['POST'])
    @jwt_required()
    def add_watchlist():
        """
        Endpoint to register new trade_platform
        ---
        parameters:
          - name: name
            in: path
            type: string
            required: true
          - name: code
            in: path
            type: string
            required: true
          - name: currency_id
            in: path
            type: int
            required: true
          - name: description
            in: path
            type: str
            required: false
        """
        serialized = ItemSerializer.parse_obj(request.json).dict()
        Item(**serialized).insert()

        return jsonify(serialized), 201


class ItemView(Resource):
    @staticmethod
    @rest_api.route('/item', methods=['GET'])
    @jwt_required()
    def list_item():
        """
        Endpoint to get item list
        ---
        parameters:
          - name: access_token
        """
        serialized = [ItemSerializer.from_orm(item).dict() for item in Item.query.all()]

        return jsonify(serialized), 200

    @staticmethod
    @rest_api.route('/item/<int:id>/', methods=['DELETE'])
    @jwt_required()
    def delete_item(id):
        """
        Endpoint to delete item
        ---
        parameters:
          - name: id
            required: true
        """
        Item.query.get(id).delete()
        return jsonify(), 204

    @staticmethod
    @rest_api.route('/item', methods=['POST'])
    @jwt_required()
    def add_item():
        """
        Endpoint to register new trade_platform
        ---
        parameters:
          - name: name
            in: path
            type: string
            required: true
          - name: code
            in: path
            type: string
            required: true
          - name: currency_id
            in: path
            type: int
            required: true
          - name: description
            in: path
            type: str
            required: false
        """
        serialized = ItemSerializer.parse_obj(request.json).dict()
        Item(**serialized).insert()

        return jsonify(serialized), 201

    @staticmethod
    @rest_api.route('/item/<int:id>/', methods=['PATCH'])
    @jwt_required()
    def update_item(id):
        """
        Endpoint to edit item
        ---
        parameters:
          - name: name
            in: path
            type: string
            required: false
          - name: code
            in: path
            type: string
            required: false
          - name: currency_id
            in: path
            type: int
            required: false
          - name: description
            in: path
            type: str
            required: false
        """
        item = Item.query.filter_by(id=id)
        item.update(request.json)
        serialized = ItemSerializer.from_orm(item.one()).dict()
        BasicModel.update()

        return jsonify(serialized), 200


class ProfileView(Resource):
    @staticmethod
    @rest_api.route('/profile', methods=['GET'])
    @jwt_required()
    def retrieve_profile():
        """
        Endpoint to get info about current user profile
        ---
        parameters:
          - name: access_token
        """
        serialized = ProfileSerializer.from_orm(Profile.query.filter_by(user_id=get_jwt_identity()).one()).dict()

        return jsonify(serialized), 200


class CurrencyView(Resource):
    @staticmethod
    @rest_api.route('/currency/<int:id>/', methods=['GET'])
    @jwt_required()
    def retrieve_currency(id):
        """
        Endpoint to get currency full info
        ---
        parameters:
          - name: name
            in: path
            type: string
            required: true
          - name: code
            in: path
            type: string
            required: true
        """
        currency = Currency.query.filter_by(id=id)
        serialized = CurrencyRetrieveSerializer.from_orm(currency.one()).dict()

        return jsonify(serialized), 200

    @staticmethod
    @rest_api.route('/currency', methods=['POST'])
    @jwt_required()
    def add_currency():
        """
        Endpoint to register new trade_platform
        ---
        parameters:
          - name: name
            in: path
            type: string
            required: true
          - name: code
            in: path
            type: string
            required: true
        """
        serialized = CurrencySerializer.parse_obj(request.json).dict()
        Currency(**serialized).insert()

        return jsonify(serialized), 201

    @staticmethod
    @rest_api.route('/currency', methods=['GET'])
    @jwt_required()
    def list_currency():
        """
        Endpoint to get currency list
        ---
        parameters:
          - name: access_token
        """
        serialized = [CurrencySerializer.from_orm(currency).dict() for currency in Currency.query.all()]

        return jsonify(serialized), 200

    @staticmethod
    @rest_api.route('/currency/<int:id>/', methods=['PATCH'])
    @jwt_required()
    def update_currency(id):
        """
        Endpoint to edit currency
        ---
        parameters:
          - name: name
            in: path
            type: string
            required: true
          - name: code
            in: path
            type: string
            required: true
        """
        currency = Currency.query.filter_by(id=id)
        currency.update(request.json)
        serialized = CurrencySerializer.from_orm(currency.one()).dict()
        BasicModel.update()

        return jsonify(serialized), 200


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
