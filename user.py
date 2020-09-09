class User:
    '''
    class that generates new instance of users
    '''

    user_list = []

    def __init__(self,name,password):
        self.name = name
        self.password = password

    def save_user(self):
         User.user_list.append(self)
