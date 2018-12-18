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
    
  
if __name__ == "__main__":
    unittest.main()