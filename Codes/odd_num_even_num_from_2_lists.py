# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 17:26:39 2021

@author: rikushwa
"""

'''
Pyhton Data Structure:
    Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
'''

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 = []

for i in range(0,len(l1),2):
    l3.append(l1[i])
    
for i in range(1,len(l2),2):
    l3.append(l2[i])
    
print(l3)