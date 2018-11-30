import os
import json
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

counter = 0;

def getQuestions():
    with open("data/words.json", "r") as the_questions:
        q = json.load(the_questions)
    return q

@app.route('/' , methods=["GET", "POST"])
def index():
    title = "Home Page"
    description = "Welcome"
    return render_template("index.html", title=title, description=description)
    
@app.route('/questions', methods=["GET","POST"])
def questions():
    
    r = getQuestions()
    results = r[counter]
    
    title = "Question Game"
    description = "Spanish Word Game"
    if request.method == "POST":
        return redirect("questions/{0}".format(request.form["answer"])) 
    
    return render_template("questions.html", title=title, description=description, results=results, counter=counter)
    
@app.route('/questions/<question>', methods=["GET","POST"])
def askQuestions(question):
    
    r = getQuestions()
    results = r[counter]
    answer = question
    title = "Question Game"
    description = "Spanish Word Game"
    
    if request.method == "POST":
        return redirect("questions") 

    return render_template("answered.html",
    title=title,
    description=description,
    results=results,
    answer=answer)
            
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