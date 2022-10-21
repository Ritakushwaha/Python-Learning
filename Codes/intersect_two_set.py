# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 18:31:38 2021

@author: rikushwa
"""

'''
Python Data Structure
Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
'''

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

value = first_set & second_set #intersection

print(value)

value_remove = first_set - value #difference

print(value_remove)