import re


def text_cleaner():
    with open('test-text.txt') as f:
        document = f.readlines()
        final = ''.join(document)

    # removes non latin characters like bullet points when it goes through
    # the nlp pipeline to prevent errors or unexpected results
    result = re.sub(r'[^\x00-\x7f]', r'', final)

    sentences = result.split('-')
    # removes hypens from when user inputs them in the app
    return sentences


sentences = text_cleaner()
