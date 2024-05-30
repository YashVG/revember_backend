from datetime import datetime
from flask import Flask, jsonify, request
from firebase_admin import credentials, firestore, initialize_app
from choose_ent import find_ents
from firebase import db  # imports firebase client
import spacy
from text_cleaner import process_the_text
from ner_file import ner
from ent_analysis import percentage_of_entities
from create_question import add_questions,  generate_answer_choices

app = Flask(__name__)


def id_generator():
    now = datetime.now()
    return now.strftime("%Y%m%d%H%M%S%f")[:-3]


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

        # add easy questions and answers
        for i in range(len(questionList)):
            doc_ref = db.collection(u'generated_questions').document(
                data[1]).collection(u'easy_questions').document(id_generator())
            doc_ref.set({
                u'name': questionList[i],
                u'answers': answer_choices[i][0]
            })

        # add medium questions and answers
        for i in range(len(questionList)):
            doc_ref = db.collection(u'generated_questions').document(
                data[1]).collection(u'medium_questions').document(id_generator())
            doc_ref.set({
                u'name': questionList[i],
                u'answers': answer_choices[i][1]
            })

        # add hard questions and answers
        for i in range(len(questionList)):
            doc_ref = db.collection(u'generated_questions').document(
                data[1]).collection(u'hard_questions').document(id_generator())
            doc_ref.set({
                u'name': questionList[i],
                u'answers': answer_choices[i][2]
            })

        return jsonify({'message': 'Data received and processed successfully!'}), 200


if __name__ == "__main__":
    nlp = spacy.load('en_core_web_lg')
    app.run()
