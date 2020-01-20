from flask_restful import reqparse, abort, Resource
import requests

parser = reqparse.RequestParser()

parser.add_argument('email', type = str)
parser.add_argument('password', type = str)

class Login(Resource):
    def get(self):
        pass
    def post(self):
        args = parser.parse_args()
        req = requests.post("http://localhost:1616/login", data = {"email" : args.email , "password" : args.password})
        return req.json()
    def put(self):
        pass
    def delete(self):
        pass