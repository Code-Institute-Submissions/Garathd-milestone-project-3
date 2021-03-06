import os
import functions
from flask import Flask, render_template, request, redirect, flash, session

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
    description = "Welcome {0}!".format(username.capitalize())
    
    #Find out the length of the game
    game_length = functions.get_file_length()

    #Logic for every time the check button is pressed
    if request.method == 'POST':
        
        form = request.form
        
        """
        Starts the game with default values when you access play the game 
        from the start game page
        """
        if form.get('start-game') == 'true':
            
            data = functions.initialize(username)
            
            return render_template('questions.html', 
            data=data,
            title=title,
            description=description)
            
        else:

            try:
                question_index = int(request.form.get('question_index'))
                score = int(request.form.get('current_score'))
                question = functions.get_question(question_index)
                
                # Check whether the answer is correct
                user_answer = request.form.get('user_answer').lower().strip()
                real_answer = question['english'].lower()
                real_question = question['spanish'].lower()
                correct = user_answer == real_answer
            
                """
                Main Game Logic
                """
                while question_index < game_length:
                    
                    #Correct Questions
                    if correct:
                        #increment score and question index
                        question_index += 1
                        score += 1
                        
                        #Displays message to my html when I get a question correct
                        flash('The translation of {0} is {1}'.format(real_question,real_answer), 'success')
                        
                        #Load Next Question
                        next_question = functions.get_question(question_index)
                        
                    #Incorrect Questions    
                    else:
                        #Increment question index
                        question_index += 1
                        
                        #Displays message to my html when I get a question wrong
                        flash('The translation of {0} is {1}. You said {2}'.format(real_question,real_answer,user_answer), 'error')
                        
                        #Load Next Question
                        next_question = functions.get_question(question_index)
    
                    #Setting up question information to be rendered to html
                    if next_question is not None:
                        data = {
                            'question_index': question_index,
                            'english': next_question['english'],
                            'spanish': next_question['spanish'],
                            'username': username,
                            'current_score': score,
                            'length': game_length
                        }
                        return render_template('questions.html', data=data,
                        title=title, description=description)
                    
                    else:
                        #Clears the messages
                        session.pop('_flashes', None)    
                
                #Set the score
                functions.set_high_score(username, score)
                
                return render_template('scores.html', 
                scores=functions.get_high_score(),
                title="Game Over", description="{0} your score is: {1}".format(username.capitalize(), score))
            
            #Game restart error handling
            except Exception as e: print("Error : {}".format(e))
            
    # Redirect to the homepage with an error if using GET
    return redirect('/')
    
    
@app.route('/scores', methods=["GET","POST"])
def scores():
    
    #Set up page
    title = "High Scores"
    description = "View the Highest Scores"
    
    #Get the high scores
    high_scores = functions.get_high_score()
    
    if request.method == 'POST':
        redirect("/")
    
    return render_template('scores.html', 
    scores=functions.get_high_score(),
    title=title,
    description=description)
    
        
app.run(
    host=os.getenv('IP'), 
    port=int(os.getenv('PORT')), 
    debug=True)