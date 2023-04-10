from datetime import datetime
from flask import Flask, jsonify, request
from firebase_admin import credentials, firestore, initialize_app
from choose_ent import find_ents
from firebase import db  # imports firebase client
import spacy
from text_cleaner import process_the_text
from ner_file import ner
from ent_analysis import percentage_of_entities
from create_question import check_length_of_answer_list, add_questions, check_empty_list, generate_answer_choices

app = Flask(__name__)

# @app.route('/hello')
# def hello():
#     return 'Hello, World!'


def id_generator():
    now = datetime.now()
    return str(now.microsecond)


@app.route('/stats', methods=['POST', 'PUT'])  # type: ignore
def stats():  # type: ignore
    if request.method == 'POST':
        data = request.get_json()
        cleanText = process_the_text(data[0], nlp)
        entities = ner(cleanText)
        stats = percentage_of_entities(cleanText, entities)
        doc_ref = db.collection(u'statistics').document(
            data[1]).collection(u'stats').document(u'advanced_stats')
        doc_ref.update({
            u'advanced_stats': firestore.ArrayUnion(stats)
        })

        return jsonify({'message': 'Data received and processed successfully!'}), 200


@app.route('/createQuestions', methods=['POST', 'PUT'])  # type: ignore
def createQuestions():  # type: ignore
    if request.method == 'POST':
        data = request.get_json()
        cleanText = process_the_text(data[0], nlp)
        entities = ner(cleanText)
        duplicateText = [i.text for i in cleanText]
        finalLstEnts = find_ents(entities)

        questionList = add_questions(finalLstEnts, duplicateText)
        print(questionList)

        answer_choices = generate_answer_choices(finalLstEnts)
        print(answer_choices)
        doc_ref = db.collection(u'test').document(
            data[1]).collection(u'questions').document(id_generator())
        doc_ref.set({
            u'name': questionList[0],
            u'answers': answer_choices[0][0]

        })
        return jsonify({'message': 'Data received and processed successfully!'}), 200


if __name__ == "__main__":
    nlp = spacy.load('en_core_web_lg')
    app.run()
