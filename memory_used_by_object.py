# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:01:15 2021

@author: rikushwa
"""

'''
Tip and Trick 3: Calculate memory is being used by an object in Python
'''
import sys

list1 = ['Scott', 'Eric', 'Kelly', 'Emma', 'Smith']
print("size of list = ",sys.getsizeof(list1))

name = 'pynative.com'
print("size of name = ",sys.getsizeof(name))