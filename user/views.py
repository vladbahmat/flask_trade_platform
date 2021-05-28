from flask_restful import Resource
from user import api

class UserView(Resource):

    @staticmethod
    @api.route('/user/register', methods=['POST'])
    def post(request):
        data = request.json
        print(data)
        #return {'hello': 'world'}