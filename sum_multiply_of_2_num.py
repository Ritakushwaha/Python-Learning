# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 15:22:44 2021

@author: rikushwa
"""

'''
Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers return their product only if the product is greater than 1000, else return their sum.
'''

def calculate(a,b):
    if a*b >= 1000:
        return a*b
    else:
        return a+b
    
    
a,b = list(map(int,input().split()))
print(calculate(a,b))