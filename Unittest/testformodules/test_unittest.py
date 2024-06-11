import unittest

from moduletotest.sum_list_module import sum_list

class TestExamples(unittest.TestCase):
    """
        Now to create the first test for our unit.
        We can perform a very basic test to see if our function
        will give us the intended result for a list with a single vlaue.
    """
    
    def test_list_add_with_one_number(self):
        #arrange
        num_list = [5]
        
        #act
        result = sum_list(num_list)
        
        #assert
        self.assertEqual(result, 5)
if __name__ == "__main__"
    unittest.main()