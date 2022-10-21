# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:04:34 2021

@author: rikushwa
"""

'''
Tip and Trick 5: Find if all elements in a list are identical
'''

listOne = [20, 20, 20, 20]
print("All element are duplicate in listOne", listOne.count(listOne[0]) == len(listOne))

listTwo = [20, 20, 20, 50]
print("All element are duplicate in listTwo", listTwo.count(listTwo[0]) == len(listTwo))