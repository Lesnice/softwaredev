import unittest
from code_test import TestTodoList
suite = unittest.TestLoader().loadTestsFromTestCase(TestTodoList)
unittest.TextTestRunner.run(suite)