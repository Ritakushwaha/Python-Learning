# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 14:00:13 2021

@author: rikushwa
"""

'''
Tip and Trick 7: How to check if all elements in a list are unique
'''

def isUnique(item):
    tempSet = set()
    return not any(i in tempSet or tempSet.add(i) for i in item)

listOne = [123, 345, 456, 23, 567]
print("All List elemtnts are Unique ", isUnique(listOne))

listTwo = [123, 345, 567, 23, 567]
print("All List elemtnts are Unique ", isUnique(listTwo))