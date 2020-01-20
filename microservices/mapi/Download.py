from flask_restful import reqparse, abort, Resource
import requests

parser = reqparse.RequestParser()

parser.add_argument('file_name', type = str)

class Download(Resource):
    def get(self, user_id):
        args = parser.parse_args()
        url = "http://localhost:9796/" + user_id + "/download"
        req = requests.get(url, data = {"file_name" : args.file_name})
        return req.json()
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass