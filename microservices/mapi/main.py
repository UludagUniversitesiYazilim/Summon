from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

import Register
import Login
import UserUpdate
import UserID
import Upload
import Download

app = Flask(__name__)
api = Api(app)

api.add_resource(Register.Register, '/register')
api.add_resource(Login.Login, '/login')
api.add_resource(UserUpdate.User_Update, '/<user_id>/update')
api.add_resource(UserID.UserID, '/userid')
api.add_resource(Upload.Upload, '/<user_id>/upload')
api.add_resource(Download.Download, '/<user_id>/download')



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9797, debug=True)