# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 16:56:27 2021

@author: rikushwa
"""

'''
Exercise 9: Check Palindrome Number
Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

'''

def is_palindrome(num):
    num = str(num)
    rev_num = num[::-1]
    if num == rev_num:
        return True
    else:
        return False
    

num = int(input())
print(is_palindrome(num))