from flask import Flask, jsonify, request
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def returnascii():
    d = {}
    inputchr = str(request.args['query'])
    answer = str(ord(inputchr))
    d['output'] = answer
    return d


if __name__ == "__main__":
    app.run()
