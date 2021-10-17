# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:16:03 2021

@author: rikushwa
"""

'''
Exercise 1: Generate 3 random integers between 100 and 999 which is divisible by 5

'''

import random

for num in range(3):
    print(random.randrange(100, 999, 5))