import numpy as np
import spacy

nlp = spacy.load("en_core_web_lg")

your_word = 'Poland'

ms = nlp.vocab.vectors.most_similar(
    np.asarray([nlp.vocab.vectors[nlp.vocab.strings[your_word]]]), n=100)

words = [nlp.vocab.strings[w] for w in ms[0][0]]

distances = ms[2]

answer_choices = words[:4]
print (answer_choices)
