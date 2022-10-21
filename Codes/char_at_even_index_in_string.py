# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 16:25:42 2021

@author: rikushwa
"""

'''
Exercise 3: Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters that are present at an even index number.
'''
def char_at_even_1(string):
    words = list(string)
    for i in words[0::2]:
        print(i)

def char_at_even_2(string):
    length = len(string)
    for i in range(0,length,2):
        print(string[i])

def char_at_even_3(string):
    for i in range(len(string)):
        if i%2 == 0:
            print(string[i])

string = str(input())

char_at_even_1(string)
char_at_even_2(string)
char_at_even_3(string)