import os
import requests
from flask import Flask, jsonify, request
from firebase_admin import credentials, firestore, initialize_app
import add_test_data



app = Flask(__name__)

# @app.route("/api", methods=['GET'])
# def hello_world():
#     d = {}
#     d['Query'] = str(request.args['Query'])
#     return jsonify(d)

@app.route("/bot", methods=['POST'])
def response():
    query = dict(request.form)['query']
    result = query
    return jsonify({"response": result})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # add_test_data.add_test_data()
