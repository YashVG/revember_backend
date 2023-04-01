from flask import Flask, jsonify, request
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)


@app.route('/get_notes', methods=['GET'])
def get_questions():
    d = {}
    inputchr = str(request.args['query'])
    d['output'] = inputchr
    return d


@app.route('/post_answers', methods=['POST'])
def send_answers():
    outputData =


if __name__ == "__main__":
    app.run()
