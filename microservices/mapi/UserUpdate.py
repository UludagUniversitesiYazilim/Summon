from flask_restful import reqparse, abort, Resource
import requests

parser = reqparse.RequestParser()

parser.add_argument('email', type = str)
parser.add_argument('password', type = str)

class User_Update(Resource):
    def get(self):
        pass
    def post(self, user_id):
        args = parser.parse_args()
        url = "http://localhost:1616/" + user_id + "/user"
        req = requests.post(url, data = {"email" : args.email , "password" : args.password})
        return req.json()
    def put(self):
        pass
    def delete(self):
        pass