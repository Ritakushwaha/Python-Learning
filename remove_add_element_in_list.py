# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 17:33:15 2021

@author: rikushwa
"""

'''
Python data structure:
    Exercise 2: Remove and add item in a list
Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
'''

l = [34, 54, 67, 89, 11, 43, 94]

print('original                :',l)
ele = l.pop(4)
print('removed 4 index element :',l)
l.insert(2,ele)
print('added element at 2 index:',l)
l.append(ele)
print('append ele at last      :',l)