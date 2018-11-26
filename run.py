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
    answers = []
    
    
    with open("data/words.json", "r") as json_data:
        questions = json.load(json_data)

    result = len(questions)
    for x in range(5):
        print "Random Numbers are: {0} ".format(random.randint(1,result))
        
        
    return render_template("index.html", 
    title=title, 
    description=description, 
    questions=questions, 
    counter=counter)
    
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