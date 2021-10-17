# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:19:26 2021

@author: rikushwa
"""

'''
Exercise 2: Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
Note you must adhere to the following conditions:
    
    The lottery number must be 10 digits long.
All 100 ticket number must be unique.
Hint: Generate a random list of 1000 numbers using randrange() and then use the sample() method to pick lucky 2 tickets.
'''

import random

lottery_list = []

for i in range(100):
    lottery_list.append(random.randrange(1000000000,9999999999))

winners = random.sample(lottery_list,2)
print('Two lucky lottery tickets are', winners)