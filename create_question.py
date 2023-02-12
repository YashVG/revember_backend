import random
from ner_file import ner

from text_cleaner import process_text

from date_gen import generate_easy_dates, generate_hard_dates, generate_medium_dates

from stats_gen import generate_numerical_answers

from choose_ent import find_ents

from find_similar_words import add_easy_words, add_hard_words, add_medium_words, add_safety_words

from list_of_ents import first_nu_ents, first_pri_ents, second_nu_ents, second_pri_ents, third_nu_ents, third_pri_ents

# change or delete later depending on pipeline built in the end
###
processed_text = process_text('test-text.txt')
entities = ner(processed_text)
duplicate_text = [i.text for i in processed_text]
final_lst_ents = find_ents()
###


def check_length_of_answer_list(answer_list):
    output_lst = []
    if len(answer_list) != 4:
        if len(answer_list) < 4:
            output_lst = add_safety_words(answer_list)
        elif len(answer_list) > 4:
            answer = answer_list[0]
            # first element remains unchanged, and is always the correct answer
            modified_list = answer_list[1:]
            if len(list(set(modified_list))) == 3:
                for i in list(set(modified_list)):
                    output_lst.append(i)

                output_lst.append(answer)
                output_lst = output_lst[::-1]
    else:
        return answer_list
    return output_lst


def add_questions(final_lst_ents):
    question_lst = []
    count = 0
    for i in final_lst_ents:
        for ent in i:

            question = duplicate_text[count].replace(ent[0], "_____")
            question_lst.append(question)

        count += 1

    return question_lst


def check_empty_list(lst4):
    # 3D matrix, like that in generate_answer_choices
    # in case one answer list is empty, duplicate another one in place of it
    for overall_answer_choices in lst4:
        for i in range(len(overall_answer_choices)):
            if len(overall_answer_choices[i]) == 0:
                try:
                    overall_answer_choices[i] = overall_answer_choices[i+1]
                except:
                    overall_answer_choices[i] = overall_answer_choices[i-1]

    return lst4


def generate_answer_choices(lst3):
    answer_lst = []
    for i in lst3:
        for ent in i:
            # print(ent[0])
            if (ent[1] in first_pri_ents) or (ent[1] in second_pri_ents) or (ent[1] in third_pri_ents):
                # print(ent[1])
                hard_answers = check_length_of_answer_list(
                    add_hard_words(ent[0]))
                medium_answers = check_length_of_answer_list(
                    add_medium_words(ent[0]))
                easy_answers = check_length_of_answer_list(
                    add_easy_words(ent[0]))
                answer_lst.append([hard_answers, medium_answers, easy_answers])
                break

            elif (ent[1] in first_nu_ents) or (ent[1] in second_nu_ents) or (ent[1] in third_nu_ents):
                if ent[1] == 'DATE':
                    hard_dates = generate_hard_dates(ent[0])
                    medium_dates = generate_medium_dates(ent[0])
                    easy_dates = generate_easy_dates(ent[0])
                    answer_lst.append([hard_dates, medium_dates, easy_dates])
                else:
                    hard_numbers = generate_numerical_answers(ent[0])
                    medium_numbers = generate_numerical_answers(ent[0])
                    easy_numbers = generate_numerical_answers(ent[0])
                    answer_lst.append(
                        [hard_numbers, medium_numbers, easy_numbers])
    answer_lst = check_empty_list(answer_lst)
    return answer_lst


# add_questions(final_lst_ents)
# print(final_lst_ents)
# print()
print(add_questions(final_lst_ents))
print(generate_answer_choices(final_lst_ents))
# print(check_length_of_answer_list(
#     ['elizabeth'])
# )
