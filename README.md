# milestone-project-3

This project was inspired through my learning of Spanish. If I found a word I didn't know I wrote it down along with the translation. I wanted to be able to design a memory / quiz game to test if I remembered the words. I also wanted the ability to record and check my most recent scores.


## UX

My UX Process was to analyze what would make this application the most user friendly and interactive.

The user's requirements are:

* As a user I want to be able to answer questions 
* As a user I want to be able to confirm my answers are correct
* As a user I want to be able to submit my score if I wish to
* As a user I want to be able to restart the list of questions


## Design

I wanted the design for this application to be minimal with the questions and answers section being the most prominent to a user. I decided to go with a minimalistic bootstrap 4 theme called [Clean Blog](https://startbootstrap.com/template-overviews/clean-blog/). 


## Features

The main feature of this web app is the ability to answer a series questions where upon conclusion users can submit their score or restart the application to re answer the list of questions.


## Features Left to Implement

Future features I would like to implement are firstly connecting the web application to a relational database.  I would then incorporate a user registration and login page. Each user account would have the ability to set the amount of questions to answer also set difficulty levels of the questions. Users would be able to add questions and answers to existing lists of questions and also create their own list of questions. 


## Technologies Used

### Python and Flask

Using Python for as much as this project as possible. Flask is the Python Framework I’m using for this application

### SCSS
Using Sass to better organise my CSS code

### Javascript and jQuery
Using jQuery and javascript for scroll to top button and showing and hiding buttons and divs

### Bootstrap 4
Using Bootstrap 4 Template from startbootstrap.com 

### Gulp
Using Gulp to watch out for SCSS changes and converting SCSS to CSS


## Testing

### Unit Testing

```
#Testing to see if questions exist
def test_find_questions_list(self):
```
This test is used to see if the list of questions exist by checking if the length of the JSON is greater than 0

``` 
#Testing to see if the counter increments
def test_counter(self):
```
This test gets the count of the counter and saves it, then increments by 1 and checks if the new count is greater than the original saved value

``` 
#Testing creation of a user score
def test_set_score(self):
```
This test is used to create a new user score. First it saves the exisitng scores, then it create a test score which is added to the score.txt file, then the score.txt file gets deleted once the test score has been confirmed that it has been added to the score.txt file. After which the original score data is restored and a new score.txt file is created with the original data in place


## Deployment

During development, all code was written in Cloud 9 and updates were saved and tested locally. Throughout the process I used GitHub to keep track of changes and to maintain version control in my code base.

The final version of my application will be pushed to Heroku


## Content
The content was inspired from the mobile app [duolingo](https://www.duolingo.com/). All the words and translations I got from duolingo


## Media
The main header image I used was found using google image search and was found on [The Great Courses Daily](www.thegreatcoursesdaily.com)


## Acknowledgements
[Start Bootstrap](https://startbootstrap.com/) - Bootstrap 4 Template *Clean Blog*

