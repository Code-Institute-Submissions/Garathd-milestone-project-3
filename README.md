# milestone-project-3

This project was inspired through my learning of Spanish. If I found a word I didn't know I wrote it down along with the English translation. I wanted to be able to design a memory / quiz game to test if I remembered the words. I also wanted the ability to record and check my most recent scores.


## UX

My UX Process was to analyze what would make this application the most user friendly and interactive.

The user's requirements are:

* As a user I want to be able to answer questions 
* As a user I want to be able to confirm my answers are correct
* As a user If my answer was incorrect then I wish to be prompted with the real answer
* As a user I want to be able to submit my score to a list of the highest scores
* As a user I want to be able to restart the game after I played already


## Design

I wanted the design for this application to be minimal with the question game being the sole focus to a user. I decided to go with a minimalistic bootstrap 4 theme called [Clean Blog](https://startbootstrap.com/template-overviews/clean-blog/). I have used jQuery to auto scroll to the bottom of each page that requires user interaction as well as using autofocused text fields to further enhance user experience


## Features

The main feature of this web app is the ability to answer a series questions where upon conclusion the users score is added to a list and if this score is in the Top 10 then feature it in the high scores page. 


## Features Left to Implement

Future features I would like to implement are firstly connecting the web application to a relational database.  I would then incorporate a user registration and login page. Each user account would have the ability to set the amount of questions to answer also set difficulty levels of the questions. Users would be able to add questions and answers to existing lists of questions and also create their own list of questions. 


## Technologies Used

### Python and Flask

Using Python for as much as this project as possible. Flask is the Python Framework I’m using for this application

### SCSS
Using Sass to better organise my CSS code

### Javascript and jQuery
Using jQuery and javascript for scroll to top button and auto scroll down on specific pages and also to hide python flash messages after 10 secs

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
#Testing to see if the default settings have been loaded
def test_start_up(self):
```
Testing game startup by checking if the username has be sucessfully entered and the game has been started
``` 
#Testing creation of a user score
def test_scoring(self):
```
This test is designed to get the high score list and copy the highest score in the list. Once the user with the highest score has been copied this data is then reused to set the high score. Since the set high score function won't write to the txt file if a record exists already then there will be no file changes and our test will pass


## Deployment

During development, all code was written in Cloud 9 and updates were saved and tested locally. Throughout the process I used GitHub to keep track of changes and to maintain version control in my code base.

The final version of my application will be pushed to Heroku


## Content
The content was inspired from the mobile app [duolingo](https://www.duolingo.com/). All the words and translations I got from duolingo


## Media
The main header image I used was found using google image search and was found on [The Great Courses Daily](www.thegreatcoursesdaily.com)


## Acknowledgements
[Start Bootstrap](https://startbootstrap.com/) - Bootstrap 4 Template *Clean Blog*

