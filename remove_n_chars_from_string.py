# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 16:25:42 2021

@author: rikushwa
"""

'''
Exercise 3: Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters that are present at an even index number.
Note: n must be less than the length of the string.
'''

def remove_n_char_from_string(n,string):
    if n < len(string):
        return string[n:]
        

n = int(input())
string = str(input())    
print(remove_n_char_from_string(n,string))
    