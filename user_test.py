import unittest  # Importing the unittest module
from user import User #Importing the User class


class TestUser(unittest.TestCase):

    """
       Test class that defines test cases for the contact class behaviours.

        Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """
    def setUp(self):
     self.new_user = User("eddah", "1234")

    """
     set up method to run before each test cases
    """
    def tearDown(self):
      User.user_list = []

    def test__init(self):
      self.assertEqual(self.new_user.name, "eddah")
      self.assertEqual(self.new_user.user_password, "1234")

      """
      test_init case to test if the object is initialized properly
      """ 

   # def test_save_user(self):
       # """
         #   test_save_user test case to test if the user object is saved into
            #the user list
            #add
           # """

        #self.new_user.save_user()  # saving the new users
        #self.assertEqual(len(User.user_list), 1)

if __name__ == '__main__':
    unittest.main()
