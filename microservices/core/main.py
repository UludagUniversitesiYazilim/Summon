from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

import Upload
import Download

app = Flask(__name__)
api = Api(app)

api.add_resource(Upload.Upload, '/<user_id>/upload')
api.add_resource(Download.Download, '/<user_id>/download')



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9796, debug=True)