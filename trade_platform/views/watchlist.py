from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from trade_platform import rest_api
from trade_platform.models import Item
from trade_platform.serializers import ItemSerializer


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