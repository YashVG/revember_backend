import os
import requests
from flask import Flask, jsonify, request
from firebase_admin import credentials, firestore, initialize_app, firestore

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello World!</h1>"


# initialise Firebase
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('test')


# @app.route('/add', methods=['POST'])
# def create():

    

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main___':
    app.run()
