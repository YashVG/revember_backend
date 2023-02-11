
from ner_file import ner

from text_cleaner import process_text

# change or delete later depending on pipeline built in the end
###
processed_text = process_text('test-text.txt')
entities = ner(processed_text)
duplicate_text = [i.text for i in processed_text]
###


def has_spaces(ent):
    # checks if entity has more than one word
    # if so, then input won't be compatible with model built
    for char in ent:
        if char.isspace():
            return True
    return False


def choose_ents(entities):
    checking_list = []
    list_of_ents = []
    for i in entities:
        list_of_notes_ents = []
        for y in i:
            if has_spaces(y[0]) == True:
                pass
            else:
                list_of_notes_ents.append(y)
                checking_list.append(y[0])

        list_of_ents.append(list_of_notes_ents)
    x = remove_duplicate_ents(list_of_ents)
    # list_of_ents will be a 3D list in every case, regardless of the input
    return x

# PREVENT SAME ENT FROM BEING CHOSEN AGAIN AND AGAIN


def remove_duplicate_ents(lst):
    flat_list = []
    for sublist in lst:
        flat_list += sublist
    vals = [i[0] for i in flat_list]
    for i in vals:
        if vals.count(i) > 2:
            for entities in lst:
                if len(entities) > 1:
                    for entity in entities:
                        if entity[0] == i:
                            entities.remove(entity)
    return lst


print(choose_ents(entities))
