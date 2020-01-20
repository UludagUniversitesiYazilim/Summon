from flask_restful import reqparse, abort, Resource
import ConnectionHelper
import datetime

parser = reqparse.RequestParser()

parser.add_argument('email', type = str)
parser.add_argument('password', type = str)

class Register(Resource):
    def get(self):
        pass
    def post(self):
        pass
    def put(self):
        connection = ConnectionHelper.connection()
        mycursor = connection.cursor()
        args = parser.parse_args()
        date = datetime.datetime.now().isoformat(' ', 'seconds')

        query = "INSERT INTO user (email, password, created_time, last_login) VALUES ('"+args.email+"','"+args.password+"','"+ date +"','"+ date +"')"

        mycursor.execute(query)

        connection.commit()

        if (mycursor.rowcount != 0):
            connection.close()
            return True
        else:
            connection.close()
            return False

    def delete(self):
        pass