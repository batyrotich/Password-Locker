import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        setup method that is  before each test case
        '''
        self.new_credentials = Credentials(
            "facebook", "eddahbaty", "fb321")

    def tearDown(self):
        '''
         cleans up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test__init(self):
        '''
        test_init test case to test if object is initialized properly
        '''
        self.assertEqual(self.new_credentials.account, "facebook")
        self.assertEqual(self.new_credentials.email, "eddahbaty")
        self.assertEqual(self.new_credentials.password, "fb321")

    def test_save_credentials(self):
        '''
         to check if credentials can be saved into the credential_list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)


if __name__ == '__main__':
    unittest.main()


