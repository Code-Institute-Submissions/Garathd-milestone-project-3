#!/usr/bin/env python
import unittest
import os
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
    
    def test_set_score(self):
        """
        This test is used to copy the scores then create a test score which is then added
        to the score.txt file and then this record is deleted once it has been found. After
        which the original score data is restored
        """
        
        score_list = "data/score.txt"
        username = "unittest"
        score = "0x01"
        result = 0
        
        #Setting up copy/backup of quiz scores
        backup_scores = question_functions.get_scores()

        #Write test data to score.txt file
        question_functions.set_score(username, score)
        
        #Writing test data to the score.txt file
        test_score = question_functions.get_scores()

        #Checking if test data has been added
        for sc in test_score:
            if sc == "unittest got a total of 0x01 points\n":
                
                #Passed the test
                result = True
                
                #Delete the score.txt file
                os.remove(score_list)
                
                #If scores are empty then create new score.txt file
                if len(backup_scores) == 0:
                    f = open(score_list, "w+")
                    f.close()
                    
                #Else copy backup of scores to a new text file named the same    
                else:
                    for old_score in backup_scores:
                        with open(score_list, "a+") as file:
                            file.writelines(old_score)
                            
            #Failed the test    
            else:
                result = False
     
        self.assertTrue(result)
        

if __name__ == "__main__":
    unittest.main()