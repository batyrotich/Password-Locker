class Credentials:
    '''
    Class that generates new instance of credentials
    '''
    credentials_list = []

    def __init__(self, account, email , password):
        self.account= account
        self.email = email
        self.password = password
        