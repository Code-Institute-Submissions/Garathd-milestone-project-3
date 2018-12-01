#!/usr/bin/env python
import os
import json
import question_functions

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/' , methods=["GET", "POST"])
def index():
    
    #Set up Page
    title = "Home Page"
    description = "Welcome"
    
    #Load Page Template
    return render_template("index.html", 
    title=title, 
    description=description)
    
@app.route('/questions', methods=["GET","POST"])
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
    
    title = "Quiz Results"
    description = "Answers to the Spanish Quiz"
    
    correct_answers = question_functions.getCorrectAnswers()
    total_questions = len(question_functions.getQuestions())
    
    if request.method == "POST":
        if request.form["restart"] == "restart":
            return redirect("questions")
        
    return render_template("results.html", 
    correct_answers=correct_answers, 
    total_questions=total_questions, 
    title=title, 
    description=description)
              
            
@app.route('/about')
def about():
    
    #Set up Page
    title = "About"
    description = "A little bit About Us"
    
    #Load Page Template
    return render_template("about.html",
    title=title, 
    description=description)
    
@app.route('/contact')
def contact():
    
    #Set up Page
    title = "Contact Page"
    description = "Get in Touch"
    
    #Load Page Template
    return render_template("contact.html", 
    title=title, 
    description=description)

app.run(
    host=os.getenv('IP'), 
    port=int(os.getenv('PORT')), 
    debug=True)