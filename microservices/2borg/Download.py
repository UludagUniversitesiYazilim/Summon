from flask_restful import reqparse, abort, Resource
import ConnectionHelper
import requests

parser = reqparse.RequestParser()

parser.add_argument('file_name', type = str)

class Download(Resource):
    def get(self, user_id):
        connection = ConnectionHelper.connection()
        mycursor = connection.cursor()
        args = parser.parse_args()

        query = "select sender,file_id from tuborg where file_name = '" + args.file_name + "' and receiver = '" + user_id + "' and active = 1"

        mycursor.execute(query)
        result = mycursor.fetchall()
        connection.close()
        download_link = "http://localhost:6565/file/" + result[0][0] + "/" + str(result[0][1])

        response = {
            "link" : download_link
        }
        
        return response
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass