import os
import json
import random
from flask import Flask, render_template, request

app = Flask(__name__)

counter = 0

@app.route('/' , methods=["GET", "POST"])
def index():
    #if request.method == "POST":
    title = "Home Page"
    description = "Spanish Word Game"
    
    questions = []

    
    with open("data/words.json", "r") as json_data:
        questions = json.load(json_data)
        
    return render_template("index.html", 
    title=title, 
    description=description, 
    questions=questions, 
    counter=counter)
    
@app.route('/getQuestions')
def getQuestions():
    
    questions = []
    
    with open("data/words.json", "r") as json_data:
        questions = json.load(json_data)
        
    return "{0}".format(questions)
    
            
@app.route('/about')
def about():
    title = "About"
    description = "A little bit About Us"
    return render_template("about.html", title=title, description=description)
    
@app.route('/contact')
def contact():
    title = "Contact Page"
    description = "Get in Touch"
    return render_template("contact.html", title=title, description=description)

@app.route('/scores')
def scores():
    title = "High Scores"
    description = "Highest Scores"
    return render_template("scores.html", title=title, description=description)
    
    

app.run(
    host=os.getenv('IP'), 
    port=int(os.getenv('PORT')), 
    debug=True)