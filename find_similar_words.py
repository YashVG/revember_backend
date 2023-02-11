import numpy as np
import spacy


def generate_similar_words(word):
    nlp = spacy.load("en_core_web_lg")
    # gets vector index of word
    vc_index = nlp.vocab.strings[word]
    # generates word vector for word in spacy's vocabulary consisting of vectors
    word_vector = np.asarray([nlp.vocab.vectors[vc_index]])
    # finds the 100 most similar words
    most_similar = nlp.vocab.vectors.most_similar(word_vector, n=100)
    # normalized version of indexes ranging from 0-1 to make processing less resource consuming
    semantic_similarities = most_similar[2]

    # finds most similar words and generates list in descending ord
    words = [nlp.vocab.strings[w] for w in most_similar[0][0]]

    # testing
    for i in range(len(list(words))):
        print(list(words)[i], semantic_similarities[0][i])

    return words, semantic_similarities


generate_similar_words('Poland')
