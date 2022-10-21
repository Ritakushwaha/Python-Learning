# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 17:34:25 2021

@author: rikushwa
"""

'''
Exercise 10: Create a new list from a two list using the following condition
Create a new list from a two list using the following condition

Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

'''

def merge_list_on_cond(lst1,lst2):
    lst=[]
    for i in lst1:
        if i%2 != 0:
            lst.append(i)
    for i in lst2:
        if i%2 == 0:
            lst.append(i)
    return lst


lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))
print(merge_list_on_cond(lst1,lst2))

'''

1 2 3 4 5

10 11 12 13 14

'''