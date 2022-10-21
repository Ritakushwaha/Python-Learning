# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 18:50:03 2021

@author: rikushwa
"""

'''
Python data structure
Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
'''

l1 = [47, 64, 69, 37, 76, 83, 95, 97]
d1 = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

for i in l1:
    if i not in d1.values():
        l1.remove(i)
        
print(l1)