# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 11:58:20 2021

@author: rikushwa
"""

'''
Tip and Trick 2: Get the difference between the two Lists
'''

list1 = ['Scott', 'Eric', 'Kelly', 'Emma', 'Smith']
list2 = ['Scott', 'Eric', 'Kelly']

set1 = set(list1)
set2 = set(list2)

print(set1,set2)

list3 = list(set1.symmetric_difference(set2))
print(list3)