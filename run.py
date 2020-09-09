#!/usr/bin/env python3.8
import random
from user import User
from credentials import Credentials

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
    