import os
import requests
from flask import Flask, jsonify, request
from firebase_admin import credentials, firestore, initialize_app, firestore

app = Flask(__name__)




# initialise Firebase
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('test')


todo_ref.add({"name": "johnny la", "age": 40})

# @app.route('/add', methods=['POST'])
# def create():


