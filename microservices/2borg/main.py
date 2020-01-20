from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

import Upload
import Download
import FileId
import SuccessfulUpload
import FileName
app = Flask(__name__)
api = Api(app)

api.add_resource(Upload.Upload, '/<user_id>/upload')
api.add_resource(Download.Download, '/<user_id>/download')
api.add_resource(SuccessfulUpload.SuccessfulUpload, '/successful_upload')
api.add_resource(FileName.File_name, '/file_name')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9795, debug=True)