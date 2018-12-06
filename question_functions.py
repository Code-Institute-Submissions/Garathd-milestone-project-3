#!/usr/bin/env python
import os
import json
from flask import render_template, redirect

#Set up highscore and questions text files
high_score_list = "data/highscore.txt"
question_list = "data/test.json"

#Setting up a counter for Questions
count = 0
correct = 0

#Get all the questions from JSON file
def getQuestions():
    with open(question_list, "r") as the_questions:
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

#Reset the questions
def resetQuestions():
    global count
    global correct
    
    count = 0
    correct = 0

#Mark Answer as Correct        
def setCorrectAnswers():
    global correct
    correct += 1

#Get correct answers value to display to webpage    
def getCorrectAnswers():
    return "{0}".format(correct)
    
#Writing the users score to text file    
def set_score(username, score):
    
    #Counting how many recent scores there is
    score_count = len(get_scores())
    
    #If there are more than 9 most recent scores than overwrite the oldest record
    if score_count >= 9:
        overwrite_score(username, score)
    else:
        #Write to text file
        data = "{0} got a total of {1} points\n".format(username, score)
        
        """Handle the process of writing data to a file"""
        with open(high_score_list, "a") as file:
            file.writelines(data)

#Get the most recent quiz scores
def get_scores():
    
    scores = []
    
    with open(high_score_list, "r") as high_scores:
        scores = high_scores.readlines()
    return scores

#Overwrite the oldest quiz score
def overwrite_score(username, score):
    
    scores = []
    scores = get_scores()
    scores.pop(0)
    
    #Delete highscore.txt file
    os.remove(high_score_list)
    
    """Handle the process of writing data to a file"""
    for sc in scores:
        """Recreating and Writing new information to highscore.txt """
        with open(high_score_list, "a") as file:
            file.writelines(sc)
            
    set_score(username, score)