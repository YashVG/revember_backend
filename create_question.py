from ner_file import ner

from text_cleaner import process_text

from choose_ent import find_ents

from find_similar_words import add_easy_words, add_hard_words, add_medium_words

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
    return question_lst


add_questions(final_lst_ents)
