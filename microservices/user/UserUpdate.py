from flask_restful import reqparse, abort, Resource
import ConnectionHelper

parser = reqparse.RequestParser()

parser.add_argument('email', type = str)
parser.add_argument('password', type = str)

class UserUpdate(Resource):
    def get(self):
        pass
    def post(self, user_id):
        connection = ConnectionHelper.connection()
        mycursor = connection.cursor()
        args = parser.parse_args()


        if (args.email != None and args.password != None):
            query = "UPDATE user SET email = '" + args.email +"',password = '"+ args.password +"' where user_id = '" + user_id + "'"
        elif (args.email != None and args.password == None):
            query = "UPDATE user SET email = '" + args.email + "' where user_id = '" + user_id + "'"
        elif (args.email == None and args.password != None):
            query = "UPDATE user SET password = '" + args.password + "' where user_id = '" + user_id + "'"
        else:
            return None

        mycursor.execute(query)

        connection.commit()
        if (mycursor.rowcount != 0):
            connection.close()
            return True
        else:
            connection.close()
            return False
    
    def put(self):
        pass
    def delete(self):
        pass