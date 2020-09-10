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
def generate_password(user):
    '''
    function to generate random password for user
    '''
    return user.generate_password()

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
    print("Hello welcome to Password Locker app. What is your name?")
    print("\n")
    ask = input(f"Hello {user_name}. Do you have an Account? YES/N0  ").lower()

    if ask == "no":
        print("Signup with password locker to have access")
        user_name = input("Enter your User name")
        create = input(f"Hello {user_name}. Do you want a generated password? YES/N0 ")
        if create == "no":
            print("-"*87)
            print(
                "|Don't mind if your password is not visible as you type. We got your password secured.|")
            print("-"*87)
            getpass.getpass()
            print("YOU ARE NOW LOGGED IN")

        while True:
            print(
                """
            USE THE SHORT CODES
    1. cc - to create a new credentials
    2. dc - to display credentials
    3. fc - to find credentials
    4. dl - to delete credentials
    5. gp - to generate a random password
    6. ex- to exit
      """)
            short_code = input("Use short-codes to navigate ").lower()

            if short_code == "cc":
                print(" Create account")
                print("-" * 10)

                print("Account ....")
                account = input(" ")

                print("Email....")
                email = input("")

                print("Enter Password")
                password = input("")

                save_credentials(create_credentials(
                    account, email, password))

                print("\n")
                print(
                    f"New Credentials {account} {email} {password} has been created")
                print("\n")
            elif short_code == "dc":

                if display_credentials():
                    print("Here is a list of all your Credentials and passwords")
                    print("\n")
                    for credentials in display_credentials():
                        print(
                            f"{credentials.account} {credentials.email}{credentials.password")
                        print("\n")
                else:
                    print("\n")
                    print(
                        "You don't have any saved credentials yet")
                    print("\n")

            elif short_code == 'fc':

                print("Enter the account username you want to search for")

                search_account_username = input()
                if check_existing_credentials(search_account_username):
                    search_credential = find_credentials(
                        search_account_username)
                    print(
                        f"{search_credentials.account} {search_credentials.email}")
                    print('-' * 20)

                    print(
                        f"Account password.......{search_credentials.account_password}")

                else:
                    print("That credential does not exist")

            elif short_code == "dl":
                print(
                    "Enter the account username of the credential you would like to delete.")
                my_delete = input("> ")
                my_del = find_credentials(my_delete)
                # Credential.credential_list.remove(my_del)
                print(f"Credential with  account username {my_delete} has been removed succefully")

            elif short_code == "gp":
                print(
                    "Please enter the account you want to generate password for ")
                social_media = input("Enter account type")

                def random_password(string_length):
                    """
                    Parameters
                    ----------
                    string_length
                    Returns
                    -------
                    """
                    letters = string.ascii_letters
                    return ".join(random.choice(letters) for i in range(string_length))"

                print(f"Your random password for {social_media} is: ", random_password(8))

            elif short_code == "ex":
                print("Logged out")

                break
    
    elif ask == "yes":
        print("Welcome back to our password locker. Enter your username and password to login")
        user_name = input("Enter username")
        print("-"*87)
        print("|Don't mind if your password is not vissible as you type. We got your password secured.|")#
        print("-"*87)
        password= getpass.getpass()
        while True:
            print("""
            USE THE SHORT CODES
    1. cc - to create a new credential
    2. dc - to display credential
    3. fc - to find credential
    4. dl - to delete credential
    5. gp - to generate a random password
    6. ex- to exit 
            """)
            short_code = input("Use short-codes to navigate ").lower()

            if short_code == "cc":
                print(" Create account")
                print("-" * 10)

                print("Account ....")
                account = input(" ")

                print("Email ....")
                email = input(" ")

                print("Enter Password")
                password = input(" ")

                save_credentials(create_credentials(account, email, password))

                print("\n")
                print(f"New Credentials {account} {email} {password} has been created")
                print("\n")

        elif short_code == "dc":

                if display_credentials():
                    print("Here is a list of all your Credentials and passwords")
                    print("\n")
                    for Credentials in display_credentials():
                        print(f"{credentials.account} {credentials.email} {password}")
                        print("\n")
                else:
                    print("\n")
                    print(
                        "You don't have any saved credentials yet. Try saving one")
                    print("\n")

        elif short_code == 'fc':

                print("Enter the account username you want to search for")

                search_account_username = input()
                if check_existing_credentials(search_account_username):
                    search_credential = find_credentials(
                        search_account_username)
                    print(
                        f"{search_credentials.account} {search_credentials.email}")
                    print('-' * 20)

                    print(
                        f"Account password.......{search_credentials.account_password}")

                else:
                    print("That credential does not exist")
        elif short_code == "dl":
                print(
                    "Enter the account username of the credential you would like to delete.")
                my_delete = input("> ")
                my_del = find_credentials(my_delete)
                # Credential.credential_list.remove(my_del)
                print(f"Credential with  account username {my_delete} has been removed succefully")

            elif short_code == "gp":
                print(
                    "Please enter the account you want to generate password for ")
                social_media = input("Enter account type")

                def random_password(string_length):
                    """
                    Parameters
                    ----------
                    string_length
                    Returns
                    -------
                    """
                    letters = string.ascii_letters
                    return ".join(random.choice(letters) for i in range(string_length))"

                print(f"Your random password for {social_media} is: ", random_password(8))

            elif short_code == "ex":
                print("Logged out")

                break
    else:
        print("Please check your entry")




if __name__ == "__main__":
    main()
