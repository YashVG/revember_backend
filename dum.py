def add_questions(finalLstEnts, duplicateText):
    questionLst = []
    count = 0
    try:
        for i in duplicateText:
            for ent in finalLstEnts:
                if str(ent[0][0]) in i:
                    question = i.replace(ent[0][0], "_____")
                    questionLst.append(question)
    except:
        for i in finalLstEnts:
            for ent in i:
                print(ent)
                question = duplicateText[count].replace(ent[0], '_____')
                print(question)
                questionLst.append(question)

            count += 1

    return questionLst
