# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:18:30 2021

@author: rikushwa
"""

'''
Exercise 7: Calculate multiplication of two random float numbers
Note:

First random float number must be between 0.1 and 1
Second random float number must be between 9.5 and 99.5
'''

import random

num1  = random.random() #return 0.0 and 1.0
print("First Random float is ", num1)
num2 = random.uniform(9.5, 99.5)
print("Second Random float is ", num2)

num3 = num1 * num2
print("Multiplication is ", num3)