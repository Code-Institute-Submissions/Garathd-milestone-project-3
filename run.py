import os
import functions
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'This should be a secret!'

@app.route('/')
def index():
    
    #Set up page
    title = "Question Game"
    description = "Start the Game"
    
    return render_template("index.html",
    title=title,
    description=description)
    
    
@app.route('/start-game/', methods=['GET', 'POST'])
def ready():
    
    #Set up page
    title = "Start Game"
    description = "Enter a Username"
    
    if request.method == 'POST':
        form = request.form
        username = form['username']
        return render_template("start.html", 
        username=username.lower(),
        title=title,
        description=description)
    #If not accessed directly    
    return redirect('/')
    

@app.route('/questions/<username>', methods=["GET","POST"])
def questions(username):
    
    #Set up page
    title = "Question Game"
    description = "Hola {0}".format(username.capitalize())
    
    #Find out the length of the game
    game_length = functions.get_file_length()

    if request.method == 'POST':
        form = request.form
        
        if form.get('start-game') == 'true':
            data = functions.initialize(username)
            return render_template('questions.html', 
            data=data,
            title=title,
            description=description)
            
        else:
            question_index = int(request.form.get('question_index'))
            score = int(request.form.get('current_score'))
            question = functions.get_question(question_index)
            
            # Check whether the answer is correct
            user_answer = request.form.get('user_answer').lower().strip()
            real_answer = question['English'].lower()
            real_question = question['Spanish'].lower()
            correct = user_answer == real_answer
        
            #Loops through the questions and displays on screen.
            #Main Game Logic
            while question_index < game_length:
                
                if correct:
                    question_index += 1
                    score += 1
                    flash('The translation of {0} is {1}'.format(real_question,real_answer), 'success')
                    next_question = functions.get_question(question_index)
                    
                else:
                    question_index += 1
                    flash('The translation of {0} is {1}. You said {2}'.format(real_question,real_answer,user_answer), 'error')
                    next_question = functions.get_question(question_index)

                if next_question is not None:
                    data = {
                        'question_index': question_index,
                        'English': next_question['English'],
                        'Spanish': next_question['Spanish'],
                        'username': username,
                        'current_score': score
                    }
                    return render_template('questions.html', data=data,
                    title=title, description=description)
            
            # Return final score and add the player to the leaderboard
            functions.set_high_score(username, score)
            return render_template('scores.html', 
            scores=functions.get_high_score(),
            title="Game Over", description="{0} your score is: {1}".format(username.capitalize(), score))
            
    # Redirect to the homepage with an error if using GET
    return redirect('/')
    
    
@app.route('/scores', methods=["GET","POST"])
def scores():
    
    #Set up page
    title = "Question Game"
    description = "High Scores"
    
    high_scores = functions.get_high_score()
    
    #Resets the Game
    if request.method == 'POST':
        # Redirect to the homepage with an error if using GET
        return redirect('/')

    return render_template('scores.html', 
    scores=functions.get_high_score(),
    title=title,
    description=description)
    
        
app.run(
    host=os.getenv('IP'), 
    port=int(os.getenv('PORT')), 
    debug=True)