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
