# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 18:27:00 2021

@author: rikushwa
"""

'''
Python Data Structure
Exercise 5: Create a Python set such that it shows the element from both lists in a pair
'''

l1 = [2, 3, 4, 5, 6, 7, 8]
l2 = [4, 9, 16, 25, 36, 49, 64]

print(set(zip(l1,l2)))