# pip install mailjet_rest
# pip install flask
from flask import Flask, jsonify, request
from mailjet_rest import Client
import os

app = Flask(__name__)

api_key = '008cc3d0969a825586688c9f8761db08'
api_secret = 'a4cd5487a1f70b3c3c0cef47d6b57963'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')

def prepare_data(email_from, email_to, file_link):
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "siladem852@gmail.com",
                    "Name": "Summon"
                },
                "To": [
                    {
                        "Email": email_to,
                        "Name": ""
                    }
                ],
                "Subject": "Summon'da yeni bir dosyan�z var!",
                "TextPart": "En b�y�k Summon Ba�ka B�y�k YOK!",
                "HTMLPart": "<h3>Sen de art�k h�zl� dosya g�nderme platformu <a href='https://www.summon.com/'>Summon</a>'�n bir par�as�s�n, ho�geldin!</h3><br />Dosyay� g�nderen : " + email_from + "<br>Dosyay� indirmek i�in <a href='" + file_link +"'>t�klay�n</a> ",
                "CustomID": "AppGettingStartedTest"
            }
        ]
    }

    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        request_data = request.get_json()
        data = prepare_data(request_data['email_from'], request_data['email_to'], request_data['file_link'])
        result = mailjet.send.create(data=data)
        return jsonify({'you sent': request_data, 'status_code': result.status_code, 'json': result.json()}), 201

if __name__ == '__main__':
    app.run(debug=False, port=80)

