from ner_file import ner

from text_cleaner import process_text

from choose_ent import find_ents

from find_similar_words import add_easy_words, add_hard_words, add_medium_words

from list_of_ents import first_nu_ents, first_pri_ents, second_nu_ents, second_pri_ents, third_nu_ents, third_pri_ents

# change or delete later depending on pipeline built in the end
###
processed_text = process_text('test-text.txt')
entities = ner(processed_text)
duplicate_text = [i.text for i in processed_text]
final_lst_ents = find_ents()
###


def add_questions(final_lst_ents):
    question_lst = []
    count = 0
    for i in final_lst_ents:
        for ent in i:
            print(ent)
            print(duplicate_text[count])
            question = duplicate_text[count].replace(ent[0], "_____")
            question_lst.append(question)

        count += 1
    print()
    for i in question_lst:
        print(i)
    return question_lst


def generate_answer_choices(lst3):
    answer_lst = []
    for i in lst3:
        for ent in i:
            # print(ent[0])
            if (ent[1] in first_pri_ents) or (ent[1] in second_pri_ents) or (ent[1] in third_pri_ents):
                # print(ent[1])
                hard_answers = add_hard_words(ent[0])
                medium_answers = add_medium_words(ent[0])
                easy_answers = add_easy_words(ent[0])
                answer_lst.append([hard_answers, medium_answers, easy_answers])
                break
                ...
            elif (ent[1] in first_nu_ents) or (ent[1] in second_nu_ents) or (ent[1] in third_nu_ents):
                if ent[1] == 'DATE':
                    print(True)
    for i in answer_lst:
        print(i)


# add_questions(final_lst_ents)
print(final_lst_ents)
print()
generate_answer_choices(final_lst_ents)
