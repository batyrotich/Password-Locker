import string
import random
class Credentials:
    '''
    class that creates instances credentials 
    '''
    credentials_list = []

    def __init__(self, account, email, password):
        self.account = account
        self.email = email
        self.password = password

    def save_credentials(self):
        '''
        self credentials in credentials_list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete credentials 
        '''
        Credentials.credentials_list.remove(self) 


    @classmethod
    def find_by_account(cls, account):
        '''
        will take an account and return the credentials associated with it
        '''
        for credentials in cls.credentials_list:
            if credentials.account == account:
                return credentials
    @classmethod
    def display_credentials(cls):
        '''
        method that  displays all credentials
        '''
        return cls.credentials_list

    def generate_password(size=7):
        '''
        method to generate 7 character password for a credential
        '''

        password = string.ascii_uppercase + string.ascii_lowercase + \
        string.digits + "</;#%@^*!~"
        gen_pass = ''.join(random.choice(password) for i in range (size))
        return gen_pass
        
    @classmethod
    def credentials_exist(cls, email):
        '''
        to search for existing account using email
        '''
        for credentials in cls.credentials_list:
            if credentials.email == email:
                return True
            return False


    
     

        
             
