from flask import Flask, jsonify, request
from firebase_admin import credentials, firestore, initialize_app
from firebase import db  # imports firebase client
import spacy
from text_cleaner import process_text

app = Flask(__name__)


def add_test_data():
    doc_ref = db.collection(u'test').document(u'alovelace')
    doc_ref.set({
        u'first': u'Ada',
        u'last': u'Lovelace',
        u'born': u'2005',
    })


@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/stats', methods=['POST', 'PUT'])  # type: ignore
def stats():  # type: ignore
    if request.method == 'POST':
        data = request.get_json()
        print(data)

        # add_test_data()
        return jsonify({'message': 'Data received and processed successfully!'}), 200


if __name__ == "__main__":
    nlp = spacy.load('en_core_web_lg')
    app.run()
