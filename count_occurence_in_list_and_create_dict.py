# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 18:11:38 2021

@author: rikushwa
"""

'''
Python Data Structure
Exercise 4: Count the occurrence of each element from a list
Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.
'''
l = [11, 45, 8, 11, 23, 45, 23, 45, 89]

count_dict = dict()

for i in l:
    cnt = l.count(i)
    if i not in count_dict:
        count_dict[i] = cnt

print(count_dict)
    
        
    
    