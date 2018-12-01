#!/usr/bin/env python
import json

#Setting up a counter for Questions
count = 0;

#Get all the questions from JSON file
def getQuestions():
    with open("data/test.json", "r") as the_questions:
        q = json.load(the_questions)
    return q

#Get the count to find out what question it is on
def getCount():
    return int(count)

#Incrementing the count
def setCount():
    
    global count
    
    #Incrementing the count
    count += 1
    
    #Get the amount of questions
    end = len(getQuestions())
    
    #Checking if at the end of the question list
    if count == end:
        count = 0

    