from flask_restful import reqparse, abort, Resource
import requests

parser = reqparse.RequestParser()

parser.add_argument('sender_email', type = str)
parser.add_argument('receiver_email', type = str)
parser.add_argument('file_name', type = str)
parser.add_argument('message', type = str)

class Upload(Resource):
    def get(self):
        pass
    def post(self):
        pass
    def put(self, user_id):
        args = parser.parse_args()
        url = "http://localhost:9796/" + user_id + "/upload"
        req = requests.put(url, data = {"sender_email" : args.sender_email, "receiver_email" : args.receiver_email, "file_name" : args.file_name, "message" : args.message})
        return req.json()
    def delete(self):
        pass