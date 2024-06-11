import unittest
from Workspace.examples import sum_list, get_middle_of_list
class TestExamples(unittest.TestCase):
    
    def test_sum_list_with_one_value(self):
        value = [7]
        
        result = sum_list(value)
        
        self.assertEqual(result, 7)
        
        
    
    def test_sum_list_with_two_values(self):
        value = [13, 7]
        
        result = sum_list(value)
        
        self.assertEqual(result, 20)
    
    def test_sum_list_with_invalid(self):
        value = ["a", 13]
        
        result = sum_list(value)
        
        self.assertEqual(result, None)
        
        
    def test_get_mid_value_with_one_value(self):
        test_list = [5] 
        result = get_middle_of_list(test_list)
        self.assertEqual(result, 5) 
          
    def test_get_mid_value_with_no_value(self):
        test_list = [] 
        result = get_middle_of_list(test_list)
        self.assertEqual(result, None)     
        
    def test_get_mid_value_with_many_value(self):
        test_list = [5, 8, 18] 
        result = get_middle_of_list(test_list)
        self.assertEqual(result, 8)     
            
if __name__ =="__main__":
    unittest.main()