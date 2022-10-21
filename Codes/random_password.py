# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:00:06 2021

@author: rikushwa
"""

'''
Exercise 6: Generate a random Password which meets the following conditions
Password length must be 10 characters long.
It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.

'''

import string, random

def random_pass():
    ran_src = string.ascii_letters + string.digits + string.punctuation
    ran_pwd = random.sample(ran_src,6)
    ran_pwd += random.sample(string.ascii_uppercase,2)
    ran_pwd += random.sample(string.digits,1)
    ran_pwd += random.sample(string.punctuation,1)
    
    ran_pass = list(ran_pwd)
    random.SystemRandom().shuffle(ran_pass)
    password = ''.join(ran_pass)
    
    return password

print(random_pass())