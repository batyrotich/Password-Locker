import unittest
from user import User

class TestUser(unittest.TestCase):
  '''
  Test class that defines test cases for users class behaviour
  '''
  def setUp(self):
    '''
    setup method to run before each test case
    '''
    self.new_user = User("eddah", "1234")
  def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []
  def test__init(self):
      '''
      test_init test case to test if the object is initialized  properly
      '''
      self.assertEqual(self.new_user.name, "eddah")
      self.assertEqual(self.new_user.password, "1234")

  def test_save_user(self):
      '''
        save_user method saves user objects to user_list
        '''
      self.new_user.save_user()
      self.assertEqual(len(User.user_list), 1)

  def test_save_multiple_user(self):
        '''
        test_save_multiple_user to sheck if  we can save multiple users
        '''
        self.new_user.save_user()
        test_user = User("Test", "password")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

  def test_delete_user(self):
        '''
        method to remove saved users
        '''
        self.new_user.save_user()
        test_user = User("Test", "password")  #new user
        test_user.save_user()

        self.new_user.delete_user()  # Deleting a user object
        self.assertEqual(len(User.user_list), 1)

if __name__ == '__main__':
  unittest.main()
