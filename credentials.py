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


            

        
             
