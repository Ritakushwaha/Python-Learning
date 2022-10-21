# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 16:33:16 2021

@author: rikushwa
"""

'''
Exercise 5: Check if the first and last number of a list is the same
Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
'''

def check_first_and_last_char_same(num_list):
    if num_list[0]==num_list[-1]:
        return True
    else:
        return False
    
num_list = list(map(int,input().split()))
print(check_first_and_last_char_same(num_list))