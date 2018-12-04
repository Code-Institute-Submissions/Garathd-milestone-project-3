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
    
    #Set up page
    title = "Quiz Results"
    description = "Answers to the Spanish Quiz"
    
    #Setup for highscores
    correct_answers = question_functions.getCorrectAnswers()
    total_questions = len(question_functions.getQuestions())
    
    #Checking if a form has been posted
    if request.method == "POST":
         print("Check request form: {0}".format(request.form))
         
         #Check if restart was selected
         if(len(request.form) == 1):
             return redirect("questions")
             
         #Write the highscore to text file
         else: 
             question_functions.set_high_score("{}\n".format(request.form["username"]))
             question_functions.set_high_score("{}\n".format(correct_answers))

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
    
@app.route('/scores')
def scores():
    
     #Set up Page
    title = "High Scores"
    description = "Checkout the Highest Scores"

    quiz_results = question_functions.get_high_scores()
    
    score_one = [quiz_results[0], quiz_results[1]]
    score_two = [quiz_results[2], quiz_results[3]]
    score_three = [quiz_results[4], quiz_results[5]]
    
    #Load Page Template
    return render_template("scores.html", 
    title=title, 
    description=description,
    score_one=score_one, 
    score_two=score_two, 
    score_three=score_three)


app.run(
    host=os.getenv('IP'), 
    port=int(os.getenv('PORT')), 
    debug=True)