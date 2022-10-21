# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 13:41:37 2021

@author: rikushwa
"""

'''
Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

'''

def reverse_integer(n):
    if n>0:
        str_n = str(n)
        str_n_rev = str_n[::-1]
        print(int(str_n_rev))

n = int(input())
reverse_integer(n)