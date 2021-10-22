# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 18:57:16 2021

@author: rikushwa
"""

'''
Python data structure
Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates
'''

d = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
l =[]

for i in d.values():
    if i not in l:
        l.append(i)
        
print(l)
