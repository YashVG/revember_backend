
from ner_file import ner

from text_cleaner import process_text
from list_of_ents import FIRST_PRI_ENTS, SECOND_PRI_ENTS, THIRD_PRI_ENTS, FIRST_NU_ENTS, SECOND_NU_ENTS, THIRD_NU_ENTS


###
processedText = process_text('test-text.txt')
entities = ner(processedText)
###


def has_spaces(ent):
    # checks if entity has more than one word
    # if so, then input won't be compatible with model built
    for char in ent:
        if char.isspace():
            return True
    return False


def choose_ents(entities):
    checkingList = []
    listOfEnts = []
    for i in entities:
        listOfNotesEnts = []
        for y in i:
            if has_spaces(y[0]) == True:
                pass
            else:
                listOfNotesEnts.append(y)
                checkingList.append(y[0])
        # list_of_ents will be a 3D list in every case, regardless of the input
        listOfEnts.append(listOfNotesEnts)
    filteredList = remove_duplicate_ents(listOfEnts)
    return filteredList


def find_ents():
    finalLst = choose_ents(entities)
    counter = 0
    for i in finalLst:
        if len(i) == 1:
            pass
        else:
            comparingEnts = []
            for ent in i:
                comparingEnts.append(ent)
            finalEnt = hierarchy_check(comparingEnts)
            finalLst.remove(i)
            finalLst.append([finalEnt])
            # re-creating into 3D matrix is better for security conventions
        counter += 1
    return finalLst


def hierarchy_check(multipleEntList):
    returnLst = []
    for i in multipleEntList:
        # check if in first priority entities
        # make sure to either break out of loop or return statement implemented
        if i[1] in FIRST_PRI_ENTS or FIRST_NU_ENTS:
            returnLst = i
            break
        else:
            if i[1] in SECOND_NU_ENTS or SECOND_PRI_ENTS:
                returnLst = i
            else:
                returnLst = i

    return returnLst


def remove_duplicate_ents(lst):
    # flat_list is a reduced 3D to 1D matrix of entities
    flatList = []
    for sublist in lst:
        flatList += sublist
    vals = [i[0] for i in flatList]
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
