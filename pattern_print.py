# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 16:51:48 2021

@author: rikushwa
"""

'''
Exercise 8: Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5

'''

def pattern_print(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i, end=' ')
        print()
    

n = int(input())
pattern_print(n)