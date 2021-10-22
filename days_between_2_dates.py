# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 15:41:58 2021

@author: rikushwa
"""

'''
Finds days between two dates
'''

from datetime import date

d0 = date(2021, 10, 22)
d1 = date(2021, 12, 7)
delta = d1 - d0
print(delta.days)