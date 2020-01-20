from flask_restful import reqparse, abort, Resource
import ConnectionHelper
import requests

parser = reqparse.RequestParser()

parser.add_argument('file_id', type = str)

class File_name(Resource):
    def get(self):
        connection = ConnectionHelper.connection()
        mycursor = connection.cursor()
        args = parser.parse_args()

        query = "SELECT file_name FROM tuborg WHERE file_id = '" + args.file_id + "'"

        mycursor.execute(query)
        result = mycursor.fetchone()

        response = {
            "file_name" : result[0]
        }
        connection.close()
        return response

    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass