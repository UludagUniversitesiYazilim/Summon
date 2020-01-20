from flask_restful import reqparse, abort, Resource
import requests

parser = reqparse.RequestParser()

parser.add_argument('email', type = str)
parser.add_argument('password', type = str)

class Register(Resource):
    def get(self):
        pass
    def post(self):
        pass
    def put(self):
        args = parser.parse_args()
        req = requests.put("http://localhost:1616/register", data = {"email" : args.email , "password" : args.password})
        return req.json()
    def delete(self):
        pass