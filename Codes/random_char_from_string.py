# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:34:27 2021

@author: rikushwa
"""

'''
Exercise 4: Pick a random character from a given String
'''

import random

def random_char(string):
    return random.choice(string)

string = str(input())
print(random_char(string))