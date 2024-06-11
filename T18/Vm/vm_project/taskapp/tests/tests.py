import unittest
from business_logic import BusinessLogic
from utilities import hash_password


class TestBusinessLogic(unittest.TestCase):
    def setUp(self):
        self.bl = BusinessLogic()
        self.bl.data_access.conn.execute("DELETE FROM users")  # Clear the users table before 
        self.bl.data_access.conn.execute("DELETE FROM data")  # Clear the data table before 
        
    def test_create_user(self):
        self.bl.create_user('testuser', 'password123', 'user')
        user = self.bl.data_access.get_user('testuser')
        self.assertIsNotNone(user)
        self.assertEqual(user[1], 'testuser')

    def test_create_user_invalid_role(self):
        self.bl.create_user('testuser', 'password123', 'invalid_role')
                            
    def test_authenticate_user(self):
        self.bl.create_user('testuser', 'password123', 'user')
        user = self.bl.authenticate_user('testuser', 'password123')
        self.assertIsNotNone(user)
        self.assertEqual(user[1], 'testuser')
                                
    def test_hash_password_empty(self):
        with self.assertRaises(ValueError):
            hash_password('')
            
if __name__ == '__main__':
    unittest.main()
