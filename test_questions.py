#!/usr/bin/env python
import unittest
import question_functions

class TestQuestions(unittest.TestCase):
    """
    Testing for Question Functionality
    """
    
    def test_find_questions_list(self):
        """
        Test to see if we can find the words.json
        """
        
        #Getting the amount of questions
        a = len(question_functions.getQuestions())
        
        #Checking if question amount is greater than 0
        self.assertGreater(a, 0)
    
    def test_counter(self):
        """
        Testing for Question Counter
        """
        
        #Getting current value of the counter
        a = question_functions.getCount()
        
        #Incrementing the counter
        question_functions.setCount()
        
        #Getting the new value of the counter
        b = question_functions.getCount()
        
        #Checking if the new value is greater than the old one
        self.assertGreater(b,a)

if __name__ == "__main__":
    unittest.main()