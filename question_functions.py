import json

def getQuestions():
    with open("data/test.json", "r") as the_questions:
        q = json.load(the_questions)
    return q

def getCount():
    with open("data/list.txt", "r") as the_count:
        q = the_count.readlines()
        qa = q[0]
        return int(qa)

def setCount():
    current = getCount()
    end = getQuestions()

    ccn = int(current)
    ccn += 1
    
    #Checking Amount of Questions
    end_scope = len(end)

    #Checking if all the questions have came up
    if end_scope == ccn:
        reset()
    else: 
        with open("data/list.txt", "w") as file:
            file.write("{0}".format(ccn))
        return current
    
def reset():
        with open("data/list.txt", "w") as file:
            file.write("0")