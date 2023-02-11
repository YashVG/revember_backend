# assume input is a list of NLP doc objects as shown in text_cleaner.py

from text_cleaner import process_text


processed_text = process_text('test-text.txt')


def ner(processed_text):
    list_of_ents = []
    for i in processed_text:
        # per sentence, the NER alg will find a list of entities in each note
        list_of_sent_ents = []
        for y in i.ents:
            # finds general entities using spacy once text is pre-processd
            # finds position of entities in respective note
            list_of_sent_ents.append([y.text, y.label_, y.start, y.end])
        list_of_ents.append(list_of_sent_ents)
    return list_of_ents
