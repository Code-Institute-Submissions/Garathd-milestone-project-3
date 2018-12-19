#!/usr/bin/env python
import unittest
import os
import functions

class TestQuestions(unittest.TestCase):
    """
    Testing for Question Functionality
    """
    
    def test_find_questions_list(self):
        """
        Test to see if we can find the json file with our word list.
        """
        questions = functions.get_question(0)
        file_length = functions.get_file_length()
        
        self.assertGreater(file_length, 0)
        
        
    def test_start_up(self):
        """
        Testing game startup by checking if the username has be sucessfully entered and 
        the game has been started
        """
        username = "Test"
        question_list =  functions.initialize(username)
        
        self.assertEqual(question_list['username'],username)
        
    
    def test_scoring(self):
        """
        This test is designed to get the high score list and copy the highest score
        in the list. Once the user with the highest score has been copied this data is then
        reused to set the high score. Since the set high score function won't write to the txt file
        if a record exists already then there will be no file changes and our test will pass
        """

        high_scores = functions.get_high_score()
            
        username = high_scores[0][0]
        score = high_scores[0][1]
            
        functions.set_high_score(username, score)
        self.assertIn((username, score), high_scores)

  
if __name__ == "__main__":
    unittest.main()