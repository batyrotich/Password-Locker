import unittest
from credentials import Credentials

class TestCredentials( unittest.TestCase):
   '''
        Test class that defines test case for class Credential behaviour
        Args:
        unittest.Testcase: TestCase class  that helps in creating test cases
   '''

   def setUp(self):
       self.new_credentials = Credentials("twitter", "eddah", "4567")
      
   def tearDown(self):
       Credentials.credentials_list = []

   def test__init(self):
       self.assertEqual(self.new_credentials.account, "twitter")
       self.assertEqual(self.new_credentials.account_username, "eddah")
       self.assertEqual(self.new_credentials.account_password, "4567")

   def test_save_credentials(self):
        """
            test_save_credentials test case to test if the credential object is saved into
            the credential list
            add
            """
        self.new_credentials.test_save_credentials()  # saving the new credential
        self.assertEqual(len(Credentials.credentials_list), 0)

   def test_save_multiple_credentials(self):

        self.new_credentials.save_credentials()
        test_credentials = Credentials("facebook", "chebet", "4900")  # new credential
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

   def test_delete_credentials(self):
        """
        test_delete_credential to test if we can remove a credential from our credential list
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("facebook", "chebet", "4900")
        test_credentials.save_credentials()
        self.new_credentials.test_delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)


if __name__ == '__main__':
    unittest.main()


