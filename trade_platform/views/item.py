from flask import jsonify, request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from trade_platform import rest_api
from trade_platform.basic_model import BasicModel
from trade_platform.models import Item
from trade_platform.serializers import ItemSerializer


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