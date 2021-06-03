from flask import jsonify, request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from trade_platform import rest_api
from trade_platform.basic_model import BasicModel
from trade_platform.models import Currency
from trade_platform.serializers import CurrencyRetrieveSerializer, CurrencySerializer


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