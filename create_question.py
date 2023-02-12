
from ner_file import ner

from text_cleaner import process_text

from date_gen import generate_easy_dates, generate_hard_dates, generate_medium_dates

from stats_gen import generate_numerical_answers

from choose_ent import find_ents

from find_similar_words import add_easy_words, add_hard_words, add_medium_words, add_safety_words

from list_of_ents import first_nu_ents, first_pri_ents, second_nu_ents, second_pri_ents, third_nu_ents, third_pri_ents

# change or delete later depending on pipeline built in the end
###
processedText = process_text('test-text.txt')
entities = ner(processedText)
duplicateText = [i.text for i in processedText]
finalLstEnts = find_ents()
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


def add_questions(finalLstEnts):
    questionLst = []
    count = 0
    for i in finalLstEnts:
        for ent in i:
            question = duplicateText[count].replace(ent[0], "_____")
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


def generate_answer_choices(lst3):
    answerLst = []
    for i in lst3:
        for ent in i:
            # print(ent[0])
            if (ent[1] in first_pri_ents) or (ent[1] in second_pri_ents) or (ent[1] in third_pri_ents):
                # print(ent[1])
                hardAnswers = check_length_of_answer_list(
                    add_hard_words(ent[0]))
                mediumAnswers = check_length_of_answer_list(
                    add_medium_words(ent[0]))
                easyAnswers = check_length_of_answer_list(
                    add_easy_words(ent[0]))
                answerLst.append([hardAnswers, mediumAnswers, easyAnswers])
                break

            elif (ent[1] in first_nu_ents) or (ent[1] in second_nu_ents) or (ent[1] in third_nu_ents):
                if ent[1] == 'DATE':
                    hardDates = generate_hard_dates(ent[0])
                    mediumDates = generate_medium_dates(ent[0])
                    easyDates = generate_easy_dates(ent[0])
                    answerLst.append([hardDates, mediumDates, easyDates])
                else:
                    hardNumbers = generate_numerical_answers(ent[0])
                    mediumNumbers = generate_numerical_answers(ent[0])
                    easyNumbers = generate_numerical_answers(ent[0])
                    answerLst.append(
                        [hardNumbers, mediumNumbers, easyNumbers])
    answerLst = check_empty_list(answerLst)
    return answerLst


# add_questions(final_lst_ents)
# print(final_lst_ents)
# print()
print(add_questions(finalLstEnts))
print(generate_answer_choices(finalLstEnts))
# print(check_length_of_answer_list(
#     ['elizabeth'])
# )
