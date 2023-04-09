from ner_file import ner
from text_cleaner import process_text


def percentage_of_the_entities():

    # change or delete later depending on pipeline built in the end
    ###
    processedText = process_text('test-text.txt')
    entities = ner(processedText)
    duplicateText = [i.text for i in processedText]
    ###
    lengthOfNotes = []
    noOfEntities = []
    percentageOfEntities = []

    # counts no of entities in each note
    for i in duplicateText:
        counter = 0
        entity = entities[duplicateText.index(i)]
        for y in entity:
            counter += 1
        noOfEntities.append(counter)
    #
    # counts number of words in each note
    for i in processedText:
        lengthOfNotes.append(len(i))
    #
    # calculates percentage of named entities per note (per word, not per character)
    for i, j in zip(noOfEntities, lengthOfNotes):
        percentage = round((i/j)*100)
        percentageOfEntities.append(percentage)

    return percentageOfEntities


def percentage_of_entities(processedText, entities):

    # change or delete later depending on pipeline built in the end
    ###
    duplicateText = [i.text for i in processedText]
    ###
    lengthOfNotes = []
    noOfEntities = []
    percentageOfEntities = []

    # counts no of entities in each note
    for i in duplicateText:
        counter = 0
        entity = entities[duplicateText.index(i)]
        for y in entity:
            counter += 1
        noOfEntities.append(counter)
    #
    # counts number of words in each note
    for i in processedText:
        lengthOfNotes.append(len(i))
    #
    # calculates percentage of named entities per note (per word, not per character)
    for i, j in zip(noOfEntities, lengthOfNotes):
        percentage = round((i/j)*100)
        percentageOfEntities.append(percentage)

    return percentageOfEntities


# print(percentage_of_the_entities())
