import os
import json

file_source = 'data/test.json'
score_source = 'data/scores.txt'
file_length = 0

def get_file_length():
    return file_length

def set_file_length(length):
    global file_length
    file_length = length

# Get the info for the next question
def get_question(index):
    with open(file_source) as json_questions:
        questions = json.loads(json_questions.read())
        set_file_length(len(questions))
        return questions[index] if index < len(questions) else None
        
# Inialize the game with some default values
def initialize(username):
    score = 0
    question = get_question(0)
    data = {
        'question_index': 0,
        'Spanish': question['Spanish'],
        'English': question['English'],
        'username': username,
        'current_score': score
    }
    return data
    
def get_high_score():
    with open(score_source) as scores:
        scores = [score for score in scores.readlines()[1:]]
        ordered_scores = []
        for score in scores:
            value = (score.split(':')[0].lower().strip(), int(score.split(':')[1].lower().strip()))
            ordered_scores.append(value)
            
        return sorted(ordered_scores, key=lambda val: val[1])[::-1][:10]
    
def set_high_score(username, score):
    high_scores = get_high_score()

    with open(score_source, 'a') as scores:
        #This make sure the user and score does not exist already
        if not(str(username), int(score)) in high_scores:
             scores.write('\n{0}:{1}'.format(str(username), str(score)))

    
    
    