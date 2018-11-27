import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/' , methods=["GET", "POST"])
def index():
    title = "Home Page"
    description = "Spanish Word Game"
    return render_template("index.html", title=title, description=description)
            
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