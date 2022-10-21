# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:03:14 2021

@author: rikushwa
"""

'''
Tip and Trick 4: Removing duplicates items from a list
'''

listNumbers = [20, 22, 24, 26, 28, 28, 20, 30, 24]
print("Original= ", listNumbers)

listNumbers = list(set(listNumbers))
print("After removing duplicate= ", listNumbers)