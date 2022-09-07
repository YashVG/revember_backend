from pickle import GET
from scipy.spatial import distance
from scipy import spatial
import numpy as np
import spacy
from firebase import db

# Load the spacy vocabulary
nlp = spacy.load("en_core_web_md")


def get_questions_and_answers(word_vec, queries):
    input_word = db.collection['users']['questions'][0]
    p = np.array([nlp.vocab[input_word].vector])

# Format the vocabulary for use in the distance function
    ids = [x for x in nlp.vocab.vectors.keys()]
    vectors = [nlp.vocab.vectors[x] for x in ids]
    vectors = np.array(vectors)
    dist = spatial.distance.cosine if np.any(word_vec) else spatial.distance.euclidean
	

def get_cosine_similarity():
    return

def get_average():
    return

def add_difficulty():
    return

def final_function():
    get_questions_and_answers(word_vec=np, queries=db)
    get_cosine_similarity()
    get_average()
    add_difficulty()