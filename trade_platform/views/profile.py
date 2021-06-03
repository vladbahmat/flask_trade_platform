from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from trade_platform import rest_api
from trade_platform.models import Profile
from trade_platform.serializers import ProfileSerializer


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