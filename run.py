#!/usr/bin/env python3.8
import random
from user import User
from credentials import Credentials
import string
import getpass

def create_user(name, password):
    '''
    function to create a new user
    '''
    new_user = User(name, password)
    return new_user

def save_user(user):
    '''
    function to save user
    '''
    user.save_user()

def find_user(name):
    '''
    function that finds a user by name and returns the user
    '''
    return User.find_by_name(name)

def delete_user(user):
    '''
    function to delete user
    '''
    user.delete_user()
def generate_password():
    '''
    function to generate a random password 
    '''
    gen_pass = Credentials.generate_password()

    return gen_pass

def create_credentials(account, email, password):
    '''
    function to create new user credentials with account email and password parameters
    '''
    new_credentials = Credentials(account, email, password)

    return new_credentials

def save_credentials(credentials):
    '''
    function to save credentials
    '''
    credentials.save_credentials()

def delete_credentials(credentials):
    '''
    function  to delete credentials
    '''
    credentials.delete_credentials()

def find_credentials(account):
    '''
    function to find credentials , it returns the account
    '''
    return Credentials.find_by_account(account)

def display_credentials():
    '''
    function to display all credentials
    '''
    return Credentials.display_all_credentials()

def main():
    print("Hello Welcome to Password Locker Application")
    print("\n")
    print(
        '''
        USE THE SHORT CODES
        1. lg - To log in
        2. ex - To exit
        '''
    )
    while True:

        short_code = input().lower()

        if short_code == 'lg':
            '''
            to enable user log in

            '''
            print("Log in to password locker")
            print("Enter User name")
            user_name = input()
            print("Enter Password")
            password = input()
            print("Confirm Password")
            confirm_password = input()

            while confirm_password != password:
                print("Password does not match")
                print("Enter your Password")
                password = input()

            else:
                print(f"{user_name} Your Log in to password locker was successful")
                print("welcome to your credentias")
                print("USE THE SHORT CODES: cc to create new credentials ex to exit")
        
        elif short_code == 'cc':
            print("Create account")
            print("-" * 10)

            print("Account e.g twitter, facebook, instagram .....")
            account = input()

            print("Email .....")
            email = input()

            print("choose password option: 'gp' to generate password, 'ep' to enter password")
            password_option = input()
            if password_option == 'ep':
                print("Enter Password")
                password = input()
            elif password_option == 'gp':
                password = generate_password()

            save_credentials(create_credentials(
                account, email, password))

            print("\n")
            print(f"New Credentials {account}  {email}  {password} has been created")

             

            










if __name__ == "__main__":
    main()
