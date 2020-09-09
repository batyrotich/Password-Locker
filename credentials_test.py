import unittest
from credentials import Credentials

class TestCredentials( unittest.TestCase):
   '''
        Test class that defines test case for class Credential behaviour
        Args:
        unittest.Testcase: TestCase class  that helps in creating test cases
   '''

   def setUp(self):
       self.new_credential = Credentials("twitter", "eddah", "4567")
      
   def tearDown(self):
       Credentials.credentials_list = []

   def test__init(self):
       self.assertEqual(self.new_credential.account, "twitter")
       self.assertEqual(self.new_credential.account_username, "eddah")
       self.assertEqual(self.new_credential.account_password, "4567")



