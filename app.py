from crypt import methods
from flask import Flask, jsonify, request
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)


@app.route('/api', methods=['GET', 'POST'])
def endpoint_handler(endpoint):
    if request.method == 'GET':
        # Handle GET request
        pass
    elif request.method == 'POST':
        # Handle POST request
        pass
    else:
        return jsonify({'error': 'Method not supported'})


if __name__ == '__main__':
    app.run(debug=True)
