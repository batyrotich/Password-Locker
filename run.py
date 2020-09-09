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
