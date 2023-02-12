
from ner_file import ner

from text_cleaner import process_text
from list_of_ents import first_pri_ents, second_pri_ents, third_pri_ents, first_nu_ents, second_nu_ents, third_nu_ents

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
        # list_of_ents will be a 3D list in every case, regardless of the input
        list_of_ents.append(list_of_notes_ents)
    filtered_list = remove_duplicate_ents(list_of_ents)
    return filtered_list


def find_ents():
    final_lst = choose_ents(entities)

    counter = 0
    for i in final_lst:
        if len(i) == 1:
            print()
            print(i[0][0])
            if i[0][0] in duplicate_text[counter]:
                print(duplicate_text[counter])

        else:

            comparing_ents = []
            print()
            for ent in i:
                print(ent)
                comparing_ents.append(ent)
            print()
            final_ent = hierarchy_check(comparing_ents)
            print(final_ent)
            final_lst.remove(i)
            final_lst.append(final_ent)
        counter += 1

    print(final_lst)


def hierarchy_check(multiple_ent_list):
    return_lst = []
    for i in multiple_ent_list:

        # check if in first priority entities
        # make sure to either break out of loop or return statement implemented
        if i[1] in first_pri_ents or first_nu_ents:
            return_lst = i
            break
        else:
            if i[1] in second_nu_ents or second_pri_ents:
                return_lst = i

            else:
                return_lst = i

    return return_lst


def remove_duplicate_ents(lst):
    # flat_list is a reduced 3D to 1D matrix of entities
    flat_list = []
    for sublist in lst:
        flat_list += sublist
    vals = [i[0] for i in flat_list]
    # checks if entity occurs more than once
    for i in vals:
        if vals.count(i) > 2:
            for entities in lst:
                # gets list of entity (2D matrix)
                if len(entities) > 1:
                    # checks if no. of entities in note is more than one to ensure that no note has no entity
                    for entity in entities:
                        # checks each entity in each note if it matches to repeated ent
                        if entity[0] == i:
                            # removes repeated ent from list of ents
                            entities.remove(entity)
    return lst


# print(add_ents(entities))
find_ents()
