
from firebase import db  # imports firebase client
import spacy
import time  # approximately 2 seconds for imports
import re

list_of_processed_notes = []

nlp = spacy.load("en_core_web_lg")

# test-text will simulate how the data will be sent from the Flutter app
# modularise this when loaded into text file
with open('test-text.txt', 'r') as file:
    data = file.read()
    data = data.split('-')
    text = data
# cleaned text with hypens removed from input data


def add_test_data():
    doc_ref = db.collection(u'test').document(u'alovelace')
    doc_ref.set({
        u'first': u'Ada',
        u'last': u'Lovelace',
        u'born': text,
    })


add_test_data()
