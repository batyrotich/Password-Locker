class Credentials:
    '''
    Class that generates new instance of credentials
    '''
    credentials_list = []

    def __init__(self, account, account_username , account_password):
        self.account= account
        self.account_username = account_username
        self.account_password = account_password
        

    def save_credentials(safe):
        '''
        save credentials method saves user objects into credentials_list 
        '''
        Credentials.credentials_list.append(safe)

    def delete_credentials(safe):
        '''
        delete credentials method delete saved credential
        '''
        Credentials.credentials_list.remove(self)
