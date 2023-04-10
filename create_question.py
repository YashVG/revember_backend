
from ner_file import ner

from text_cleaner import process_text

from date_gen import generate_easy_dates, generate_hard_dates, generate_medium_dates

from stats_gen import generate_numerical_answers

from choose_ent import find_ents

from find_similar_words import add_easy_words, add_hard_words, add_medium_words, add_safety_words

from list_of_ents import FIRST_NU_ENTS, FIRST_PRI_ENTS, SECOND_NU_ENTS, SECOND_PRI_ENTS, THIRD_NU_ENTS, THIRD_PRI_ENTS

# change or delete later depending on pipeline built in the end
###
# processedText = process_text('test-text.txt')
# entities = ner(processedText)
# duplicateText = [i.text for i in processedText]
# finalLstEnts = find_ents(entities)
###


def check_length_of_answer_list(answerList):
    outputLst = []
    if len(answerList) != 4:
        if len(answerList) < 4:
            outputLst = add_safety_words(answerList)
        elif len(answerList) > 4:
            answer = answerList[0]
            # first element remains unchanged, and is always the correct answer
            modifiedList = answerList[1:]
            if len(list(set(modifiedList))) == 3:
                for i in list(set(modifiedList)):
                    outputLst.append(i)

                outputLst.append(answer)
                outputLst = outputLst[::-1]
    else:
        return answerList
    return outputLst


def add_questions(finalLstEnts, duplicateText):
    questionLst = []
    count = 0
    try:
        for i in duplicateText:
            for ent in finalLstEnts:
                if str(ent[0][0]) in i:
                    question = i.replace(ent[0][0], "_____")
                    questionLst.append(question)
    except:
        for i in finalLstEnts:
            for ent in i:
                print(ent)
                question = duplicateText[count].replace(ent[0], '_____')
                print(question)
                questionLst.append(question)

            count += 1

    return questionLst


def check_empty_list(lst4):
    # 3D matrix, like that in generate_answer_choices
    # in case one answer list is empty, duplicate another one in place of it
    for overallAnswerChoices in lst4:
        for i in range(len(overallAnswerChoices)):
            if len(overallAnswerChoices[i]) == 0:
                try:
                    overallAnswerChoices[i] = overallAnswerChoices[i+1]
                except:
                    overallAnswerChoices[i] = overallAnswerChoices[i-1]

    return lst4


def generate_answer_choices(listOfEntities):
    answerLst = []
    for i in listOfEntities:
        for ent in i:
            # print(ent[0])
            if (ent[1] in FIRST_PRI_ENTS) or (ent[1] in SECOND_PRI_ENTS) or (ent[1] in THIRD_PRI_ENTS):
                # print(ent[1])
                easyAnswers = check_length_of_answer_list(
                    add_easy_words(ent[0]))
                mediumAnswers = check_length_of_answer_list(
                    add_medium_words(ent[0]))
                hardAnswers = check_length_of_answer_list(
                    add_hard_words(ent[0]))

                answerLst.append([easyAnswers, mediumAnswers, hardAnswers])
                break

            elif (ent[1] in FIRST_NU_ENTS) or (ent[1] in SECOND_NU_ENTS) or (ent[1] in THIRD_NU_ENTS):
                if ent[1] == 'DATE':
                    easyDates = generate_easy_dates(ent[0])
                    mediumDates = generate_medium_dates(ent[0])
                    hardDates = generate_hard_dates(ent[0])
                    answerLst.append([easyDates, mediumDates, hardDates])
                else:
                    easyNumbers = generate_numerical_answers(ent[0])
                    mediumNumbers = generate_numerical_answers(ent[0])
                    hardNumbers = generate_numerical_answers(ent[0])

                    answerLst.append(
                        [easyNumbers, mediumNumbers, hardNumbers])
    answerLst = check_empty_list(answerLst)
    return answerLst


# x = add_questions(finalLstEnts, duplicateText)
# y = generate_answer_choices(finalLstEnts)
# print(check_length_of_answer_list(
#     ['elizabeth'])
# )
# for i in x:
#     print(i)
# for i in y:
#     print(i)
