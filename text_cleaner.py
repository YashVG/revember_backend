# as opposed to using spacy's provided text cleaner
# I developed mine that was more time efficient and
# specific to my solution

import spacy
import re


def process_text(text_dir):
    listOfProcessedNotes = []

    nlp = spacy.load("en_core_web_lg")

# test-text will simulate how the data will be sent from the Flutter app
# modularise this when loaded into text file
    with open(text_dir, 'r') as file:
        data = file.read()
        data = data.split('-')
        text = data
# cleaned text with hypens removed from input data

# regex comands to remove non-Latin characters
# modularise this mini function
    for i in text:
        i = re.sub(r'[^\x00-\x7f]', r'', i)
    # removes unecessary new lines with null space
        for y in i:
            i.replace('\n', '')
    # removes any leading or trailing whitespaces inputted by the user
        i = i.strip()
        listOfProcessedNotes.append(nlp(i))

    # removes first element which is always a blank space
    listOfProcessedNotes.pop(0)

    return listOfProcessedNotes
