# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 19:00:18 2021

@author: rikushwa
"""

'''
Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
'''

l = [87, 45, 41, 65, 94, 41, 99, 94]

s = set(l)

tup = tuple(s)

mini = min(tup)
maxi = max(tup)

print(mini,maxi)