# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 16:40:32 2021

@author: rikushwa
"""

'''
Exercise 6: Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those numbers which are divisible by 5

'''

def num_divisible_by_5(num_list):
    for i in num_list:
        if i%5 ==0:
            print(i)


num_list = list(map(int, input().split()))
num_divisible_by_5(num_list)