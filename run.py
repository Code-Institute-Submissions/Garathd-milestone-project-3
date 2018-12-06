#!/usr/bin/env python
import os
import json
import question_functions

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

""" 
Redirects the homepage to the questions page.
The Questions Page is the real homepage.
This is just done for the purpose of routing.
"""
@app.route('/')
def index():
    return redirect("questions")
    

@app.route('/questions' , methods=["GET", "POST"])
def questions():
    
    #Set up Page
    title = "Question Game"
    description = "Spanish Word Game"
    
    #Find out what question it's on
    counter = question_functions.getCount()
    
    #Get the questions
    amount = question_functions.getQuestions()
    
    #Get current question
    results = amount[counter]
    
    #Get correct answers
    correct = question_functions.getCorrectAnswers()
    
    #Submit answer
    if request.method == "POST":
        return redirect("questions/{0}".format(request.form["answer"])) 
        
    #Load Page Template
    return render_template("questions.html", 
    title=title, 
    description=description, 
    results=results, 
    counter=counter, 
    amount=len(amount),
    correct=correct)


@app.route('/questions/<question>', methods=["GET","POST"])
def askQuestions(question):
    
    #Set up Page
    title = "Question Game"
    description = "Spanish Word Game"

    #Find out what question it's on
    counter = question_functions.getCount()

    #Get the questions
    amount = question_functions.getQuestions()
    
    #Get current question
    results = amount[counter]
    
    #Get user answer
    answer = question

    #Check if users answer is correct
    if results["English"] == answer:
        passed = True
        mark = "Well Done, You answered correctly!"
    else:
        passed = False
        mark = "Your answer is incorrect!"

    #Increment count to get the next question    
    if request.method == "POST":
        if passed == True:
            question_functions.setCorrectAnswers()
            
        end_point = counter 
        end_point +=1

        #Check if the quiz is finished  
        if end_point == len(amount):
            return redirect("results") 
        else:
            question_functions.setCount()
            return redirect("questions")     
            
    #Load Page Template
    return render_template("answered.html",
    title=title,
    description=description,
    results=results,
    answer=answer,
    mark=mark)
    
            
@app.route('/results', methods=["GET","POST"])
def results():
    
    #Set up page
    title = "Quiz Results"
    description = "Answers to the Spanish Quiz"
    
    #Setup for highscores
    correct_answers = question_functions.getCorrectAnswers()
    total_questions = len(question_functions.getQuestions())
    
    #Reset Questions
    question_functions.resetQuestions()
    
    #Checking if a form has been posted
    if request.method == "POST":
         print("Check request form: {0}".format(request.form))
         
         #Check if restart was selected
         if(len(request.form) == 1):
             return redirect("questions")
             
         #Write the highscore to text file
         else: 
             question_functions.set_score(request.form["username"], correct_answers)
             return redirect("scores")

    #Load Page Template
    return render_template("results.html", 
    correct_answers=correct_answers, 
    total_questions=total_questions, 
    title=title, 
    description=description)
    
              
@app.route('/scores')
def scores():
    
    #Set up Page
    title = "Recent Scores"
    description = "Checkout the Most Recent Scores"

    #Get the 10 most recent scores
    quiz_results = question_functions.get_scores()
    
    #Load Page Template
    return render_template("scores.html", 
    title=title, 
    description=description,
    quiz_results=quiz_results)
    

@app.route('/about')
def about():
    
    #Set up Page
    title = "About Page"
    description = "Site Description and Info"
    
    #Load Page Template
    return render_template("about.html",
    title=title,
    description=description)
    

app.run(
    host=os.getenv('IP'), 
    port=int(os.getenv('PORT')), 
    debug=True)