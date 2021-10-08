# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 16:45:00 2021

@author: rikushwa
"""

'''
Exercise 7: Return the count of a given substring from a string
Write a program to find how many times substring “Emma” appears in the given string.

'''



def count_substring_in_string(string, sub_str):    
    return string.count(sub_str)

string = str(input())
sub_str = str(input())
print(count_substring_in_string(string, sub_str))