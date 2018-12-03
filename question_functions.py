#!/usr/bin/env python
import json
from flask import render_template, redirect

#Setting up a counter for Questions
count = 0
correct = 0

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
    global correct
    
    #Incrementing the count
    count += 1
    
    #Get the amount of questions
    end = len(getQuestions())
    
    #Checking if at the end of the question list and reset all values
    if count == end:
        count = 0
        correct = 0

#Mark Answer as Correct        
def setCorrectAnswers():
    global correct
    correct += 1

#Get correct answers value to display to webpage    
def getCorrectAnswers():
    return "{0}".format(correct)
    
#Writing the highscores to text file    
def set_high_score(data):
    filename = "data/highscore.txt"
    """Handle the process of writing data to a file"""
    with open(filename, "a") as file:
        file.writelines(data)
        
        
