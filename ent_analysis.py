from ner_file import ner
from text_cleaner import process_text


def percentage_of_entities():

    # change or delete later depending on pipeline built in the end
    ###
    processed_text = process_text('test-text.txt')
    entities = ner(processed_text)
    duplicate_text = [i.text for i in processed_text]
    ###

    length_of_notes = []
    no_of_entities = []
    percentage_of_entities = []

    # counts no of entities in each note
    for i in duplicate_text:
        counter = 0
        entity = entities[duplicate_text.index(i)]
        for y in entity:
            counter += 1
        no_of_entities.append(counter)
    #
    # counts number of words in each note
    for i in processed_text:
        length_of_notes.append(len(i))
    #
    # calculates percentage of named entities per note (per word, not per character)
    for i, j in zip(no_of_entities, length_of_notes):
        percentage = round((i/j)*100)
        percentage_of_entities.append(percentage)

    return percentage_of_entities


print(percentage_of_entities())
