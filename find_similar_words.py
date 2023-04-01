import numpy as np
import spacy
from cosine_sim import word2vec, cosdis
import random

# can't simplify easy, medium or hard functions because modularizing it further results in failed API calls


def generate_similar_words(word):
    # TODO: remove later if needed
    nlp = spacy.load("en_core_web_lg")
    # gets vector index of word
    vcIndex = nlp.vocab.strings[word]
    # generates word vector for word in spacy's vocabulary consisting of vectors
    wordVector = np.asarray([nlp.vocab.vectors[vcIndex]])
    # finds the 200 most similar words
    mostSimilar = nlp.vocab.vectors.most_similar(wordVector, n=200)
    # normalized version of indexes ranging from 0-1 to make processing less resource consuming
    semanticSimilarities = mostSimilar[2]

    # finds most similar words and generates list in descending ord
    words = [nlp.vocab.strings[w] for w in mostSimilar[0][0]]

    # testing
    # for i in range(len(list(words))):
    #     print(list(words)[i], semantic_similarities[0][i])

    return words, semanticSimilarities


def add_hard_words(inp):
    answerChoices = [inp]
    inpVector = word2vec(inp)
    similarWords, similarDistances = generate_similar_words(inp)
    for i in range(len(list(similarWords))):
        # checks if decapitalized word generated is the same as input, or if semantic similarity is equal to 1
        if (similarWords[i]).lower() == inp.lower() or similarDistances[0][i] == 1.0:
            # passes any words that are the same as the input
            pass
        else:
            wordVector = word2vec(similarWords[i])
            # if cos sim is greater than 0.75, that means the word is very similar
            # therefore skip over to next word in list
            if cosdis(inpVector, wordVector) > 0.75:
                pass
            else:

                # adds words with given range below
                if 0.7 <= similarDistances[0][i] <= 0.79999:
                    answerChoices.append(similarWords[i])
                else:
                    pass
    # create new lists to deal with duplicates with different capitalizations
    return answer_choosing(inp, answerChoices)


def add_medium_words(inp):
    answerChoices = [inp]
    inpVector = word2vec(inp)
    similarWords, similarDistances = generate_similar_words(inp)
    for i in range(len(list(similarWords))):
        wordVector = word2vec(similarWords[i])
        # if cos sim is greater than 0.75, that means the word is very similar
        # therefore skip over to next word in list
        if cosdis(inpVector, wordVector) > 0.75:
            pass
        else:

            # adds words with given range below
            if 0.58 <= similarDistances[0][i] <= 0.7:
                answerChoices.append(similarWords[i])
            else:
                pass
    # create new lists to deal with duplicates with different capitalizations
    return answer_choosing(inp, answerChoices)


def add_easy_words(inp):
    answerChoices = [inp]
    inpVector = word2vec(inp)
    similarWords, similarDistances = generate_similar_words(inp)
    for i in range(len(list(similarWords))):
        word_vector = word2vec(similarWords[i])
        # if cos sim is greater than 0.75, that means the word is very similar
        # therefore skip over to next word in list
        if cosdis(inpVector, word_vector) > 0.75:
            pass
        else:
            # print(sd[0][i])
            # adds words with given range below
            if similarDistances[0][i] <= 0.57:
                answerChoices.append(similarWords[i])
            else:
                pass
    # create new lists to deal with duplicates with different capitalizations
    return answer_choosing(inp, answerChoices)


def add_safety_words(list_of_answers):
    output = []
    # list_of_answers will always be less than 4
    noOfExtraWords = 4 - len(list_of_answers)
    similarWords, similarDistances = generate_similar_words(list_of_answers[0])
    for i in range(len(list(similarWords))):
        if 0.58 <= similarDistances[0][i] <= 0.7:
            output.append((similarWords[i]).lower())

    output = random.sample(output, noOfExtraWords)
    output.append(list_of_answers[0])
    output = output[::-1]
    return output


def answer_choosing(inp, answer_choices):
    rawAnswerChoices = [inp.lower()]

    # decapitalizes everything, and ensures no duplicate input
    cleaningList = []
    for i in answer_choices:
        cleaningList.append(i.lower())
    newCleaningList = list(set(cleaningList))
    newCleaningList.remove(inp.lower())
    if len(newCleaningList) > 3:
        # adds three random words from answer list to output list
        # if initial list is more than 3
        newList = random.sample(newCleaningList, 3)
        for i in newList:
            rawAnswerChoices.append(i)
        return rawAnswerChoices
    else:
        # if not bigger than three, just return initial list
        # and filter in final answer generation
        return cleaningList
