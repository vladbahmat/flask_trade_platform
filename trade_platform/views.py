from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from app import db
from trade_platform import rest_api
from flask import request, jsonify

from trade_platform.models import User, Currency
from trade_platform.serializers import UserSerializer, CurrencySerializer


class CurrencyView(Resource):
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
        data = request.json
        currency = Currency(**data)
        db.session.add(currency)
        db.session.commit()

        return jsonify(CurrencySerializer.from_orm(currency).dict()), 201

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
        data = request.json
        currency = Currency.query.filter_by(id=id)
        currency.update(data)
        serialized = CurrencySerializer.from_orm(currency.one()).dict()
        db.session.commit()

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
        data = request.json
        user = User.query.filter_by(id=id).delete()
        db.session.commit()

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
        data = request.json
        user = User.query.filter_by(id=id)
        user.update(data)
        serialized = UserSerializer.from_orm(user.one()).dict()
        db.session.commit()

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

        return jsonify({'access_token':token}), 200
