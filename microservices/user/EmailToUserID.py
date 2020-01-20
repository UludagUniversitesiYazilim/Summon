from flask_restful import reqparse, abort, Resource
import ConnectionHelper

parser = reqparse.RequestParser()

parser.add_argument('email', type = str)

class UserID(Resource):
    def get(self):

        connection = ConnectionHelper.connection()
        mycursor = connection.cursor()
        args = parser.parse_args()
        
        query = "select user_id from user where email = '" + args.email + "'"

        mycursor.execute(query)
        result = mycursor.fetchone()

        response = {
            "user_id" : result[0]
        }
        connection.close()
        return response
    
    def post(self):
        pass
    
    def put(self):
        pass

    def delete(self):
        pass
