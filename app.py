from crypt import methods
from flask import Flask, jsonify, request
from firebase_admin import credentials, firestore, initialize_app
import add_test_data
from ocr import scan_text
from difficulty import final_function




app = Flask(__name__)

# @app.route("/api", methods=['GET'])
# def hello_world():
#     d = {}
#     d['Query'] = str(request.args['Query'])
#     return jsonify(d)

@app.route("/bot", methods=['POST']) #test query to see if heroku api functional
def response():
    query = dict(request.form)['query']
    result = query
    return jsonify({"response": result})

@app.route('/question_generator', methods=['GET', 'POST', 'UPDATE'])
def question_generator():
    question_generator.generate_questions() #rename function to something more distinct from above
    query = dict(request.form)['generated_questions']['$topic_hash']['questions']['$questionID']  # type: ignore
    #added $ as it will be passed into Flutter for querying
    question = query #make query above less clunky, use other references like in frontend
    answer1 = query['answers'][0]  # type: ignore #check why it gives incompatible with slices later
    answer2 = query['answers'][1] # type: ignore
    answer3 = query['answers'][2] # type: ignore
    answer4 = query['answers'][3] # type: ignore
    return jsonify({"question_name": question, "answer1": answer1, "answer2": answer2, "answer3": answer3, "answer4": answer4})
    # sends to api link in flutter, where it gets added to db

@app.route('/difficulty_measure', methods=['GET', 'POST']) # type: ignore #TODO: rename methods to avoid confusion
def difficulty_measure():
    final_function() # re-do other functions like this where querying is done in separate files


# @app.route('/ocr', methods=['GET', 'POST'])
# def return_text():
#     scan_text()

# FIX THIS IMMEDIATELY




if __name__ == '__main__':
    app.run()
    # add_test_data.add_test_data()
