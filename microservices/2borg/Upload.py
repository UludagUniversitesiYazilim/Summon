from flask_restful import reqparse, abort, Resource
import ConnectionHelper
import requests
import json

parser = reqparse.RequestParser()

parser.add_argument('sender_email', type = str)
parser.add_argument('receiver_email', type = str)
parser.add_argument('file_name', type = str)

class Upload(Resource):
    def get(self):
        pass
    def post(self):
        pass
    def put(self, user_id):
        connection = ConnectionHelper.connection()
        mycursor = connection.cursor()
        args = parser.parse_args()

        req_sender = requests.get("http://localhost:1616/userid", data = {"email" : args.sender_email})
        req_receiver = requests.get("http://localhost:1616/userid", data = {"email" : args.receiver_email})

        print(type(req_sender),req_sender.text)
        snd = req_sender.json()
        rcv = req_receiver.json()
        query = "INSERT INTO tuborg (sender,receiver,file_name,active,download_count) VALUES ('{snd['user_id']}','{rcv['user_id']}','{ args.file_name }',0,0)"
        mycursor.execute(query)

        connection.commit()

        if (mycursor.rowcount != 0):
            query = "SELECT file_id FROM tuborg WHERE file_name = '" + args.file_name + "'"

            mycursor.execute(query)
            result = mycursor.fetchone()

            info = {
                "sender_id" : snd['user_id'],
                "receiver_id" : rcv['user_id'],
                "file_id" : result[0]
            }

            connection.close()
            print(info)
            return info
        else:
            info = {
                "sender_id" : "None",
                "receiver_id" : "None",
                "file_id" : "None"
            }
            print("HATA!!!")
            connection.close()
            return info
    def delete(self):
        pass