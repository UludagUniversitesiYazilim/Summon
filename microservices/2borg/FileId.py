from flask_restful import reqparse, abort, Resource
import ConnectionHelper
import requests

parser = reqparse.RequestParser()

parser.add_argument('file_name', type = str)

class File_id(Resource):
    def get(self, user_id):
        connection = ConnectionHelper.connection()
        mycursor = connection.cursor()
        args = parser.parse_args()

        query = "SELECT file_id FROM 2borg WHERE file_name = '" + args.file_name + "'"

        mycursor.execute(query)
        result = mycursor.fetchone()

        response = {
            "file_id" : result[0]
        }
        connection.close()
        return response

    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass