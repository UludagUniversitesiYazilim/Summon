from flask_restful import reqparse, abort, Resource
import datetime
import ConnectionHelper

parser = reqparse.RequestParser()

parser.add_argument('email', type = str)
parser.add_argument('password', type = str)

class Login(Resource):
    def get(self):
        pass
    
    def post(self):
        connection = ConnectionHelper.connection()
        mycursor = connection.cursor()
        args = parser.parse_args()

        query = "select user_id from user where email = '" + args.email + "' and password = '" + args.password + "'"

        mycursor.execute(query)
        result = mycursor.fetchone()
        connection.close()
        if (result != None):
            return {'user_id' : result[0]}
        else:
            return False
        
    def put(self):
        pass

    def delete(self):
        pass
