from flask_restful import reqparse, abort, Resource
import requests

parser = reqparse.RequestParser()

parser.add_argument('email', type = str)

class UserID(Resource):
    def get(self):
        args = parser.parse_args()
        req = requests.get("http://localhost:1616/userid", data = {"email" : args.email})
        return req.json()
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass