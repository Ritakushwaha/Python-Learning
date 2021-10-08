# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 15:22:44 2021

@author: rikushwa
"""

'''
Exercise 2: Print the sum of the current number and the previous number
Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
'''

def calculate(n):
    previous = 0
    for i in range (n):
        print(f'Sum of {previous} and {i} is {previous+i}')
        previous = i
    
    
n = int(input()) #input a range value
calculate(n)