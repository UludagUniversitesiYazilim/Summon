from flask_restful import reqparse, abort, Resource
import ConnectionHelper
import requests

parser = reqparse.RequestParser()

parser.add_argument('file_name', type = str)

class SuccessfulUpload(Resource):
    def get(self):
        pass
    def post(self):
        connection = ConnectionHelper.connection()
        mycursor = connection.cursor()
        args = parser.parse_args()

        query = "SELECT active FROM tuborg WHERE file_name = '" + args.file_name + "'"

        mycursor.execute(query)
        result = mycursor.fetchone()
        print(result)
        if(result[0] == 0):
            connection.close()

            connection2 = ConnectionHelper.connection()
            mycursor2 = connection2.cursor()

            query = "UPDATE tuborg SET active = 1 where file_name = '" + args.file_name + "'"

            mycursor2.execute(query)

            connection2.commit()

            connection2.close()
            response = {
                "result" : "True"
            }

            return response
    def put(self):
        pass
    def delete(self):
        pass