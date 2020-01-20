from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

import EmailToUserID
import UserUpdate
import Login
import Register

app = Flask(__name__)
api = Api(app)

api.add_resource(EmailToUserID.UserID, '/userid')
api.add_resource(UserUpdate.UserUpdate, '/<user_id>/user')
api.add_resource(Login.Login, '/login')
api.add_resource(Register.Register, '/register')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1616, debug=True)