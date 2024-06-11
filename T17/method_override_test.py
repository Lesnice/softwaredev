import unittest
from unittest.mock import patch
from io import StringIO
from method_override import Adult, Child

class TestAdultChild(unittest.TestCase):
    def setUp(self):
        #create inputs for each instance before each test
        self.adult = Adult("John Doe", 30, "blue", "brown")#
        self.child = Child("Jane Doe", 10, "green", "black")
        
    #create test for adult attributes inputs   
    def test_adult_attributes(self):
        self.assertEqual(self.adult.name, "John Doe")
        self.assertEqual(self.adult.age, 30)
        self.assertEqual(self.adult.eye_colour, "blue")
        self.assertEqual(self.adult.hair_colour, "brown")
    #create test for child attribute inputs   
    def test_child_attributes(self):
        self.assertEqual(self.child.name, "Jane Doe")
        self.assertEqual(self.child.age, 10)
        self.assertEqual(self.child.eye_colour, "green")
        self.assertEqual(self.child.hair_colour, "black")
        #test adult attribute output
    @patch('sys.stdout', new_callable=StringIO)
    def test_adult_can_drive(self, mock_stdout):
        self.adult.can_drive()
        self.assertEqual(mock_stdout.getvalue().strip(), "John Doe  is old enough to drive")
        #test child attribute outputs
    @patch('sys.stdout', new_callable=StringIO)
    def test_child_can_drive(self, mock_stdout):
        self.child.can_drive()
        self.assertEqual(mock_stdout.getvalue().strip(), "You are too young to drive")
        
if __name__ == '__main__':
    unittest.main()  