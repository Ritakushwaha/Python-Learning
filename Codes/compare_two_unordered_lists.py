# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:05:43 2021

@author: rikushwa
"""

'''
Tip and Trick 6: How to efficiently compare two unordered lists
'''

from collections import Counter

one = [33, 22, 11, 44, 55]
two = [22, 11, 44, 55, 33]

print("is two list are equal", Counter(one) == Counter(two))