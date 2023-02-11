import numpy as np
import spacy
from cosine_sim import word2vec, cosdis
import random


def generate_similar_words(word):
    # TODO: remove later if needed
    nlp = spacy.load("en_core_web_lg")
    # gets vector index of word
    vc_index = nlp.vocab.strings[word]
    # generates word vector for word in spacy's vocabulary consisting of vectors
    word_vector = np.asarray([nlp.vocab.vectors[vc_index]])
    # finds the 100 most similar words
    most_similar = nlp.vocab.vectors.most_similar(word_vector, n=200)
    # normalized version of indexes ranging from 0-1 to make processing less resource consuming
    semantic_similarities = most_similar[2]

    # finds most similar words and generates list in descending ord
    words = [nlp.vocab.strings[w] for w in most_similar[0][0]]

    # testing
    # for i in range(len(list(words))):
    #     print(list(words)[i], semantic_similarities[0][i])

    return words, semantic_similarities


def add_hard_words(inp):
    answer_choices = [inp]
    inp_vector = word2vec(inp)
    sw, sd = generate_similar_words(inp)
    for i in range(len(list(sw))):
        # checks if decapitalized word generated is the same as input, or if semantic similarity is equal to 1
        if (sw[i]).lower() == inp.lower() or sd[0][i] == 1.0:
            # passes any words that are the same as the input
            pass
        else:
            word_vector = word2vec(sw[i])
            # if cos sim is greater than 0.8, that means the word is very similar
            # therefore skip over to next word in list
            if cosdis(inp_vector, word_vector) > 0.75:
                pass
            else:
                # print(sd[0][i])
                # adds words with given range below
                if 0.7 <= sd[0][i] <= 0.79999:
                    answer_choices.append(sw[i])
                else:
                    pass
    # create new lists to deal with duplicates with different capitalizations
    hard_answer_choices = [inp.lower()]
    cleaning_list = []
    for i in answer_choices:
        cleaning_list.append(i.lower())
    cleaning_list = list(set(cleaning_list))
    cleaning_list.remove(inp.lower())
    # for i in cleaning_list:
    #     hard_answer_choices.append(i)
    new_list = random.sample(cleaning_list, 3)
    for i in new_list:
        hard_answer_choices.append(i)
    return hard_answer_choices

# after getting lots of answers, the next function will compare the word to the input
# and determine whether it's the same type of word


print(add_hard_words('Russia'))
