# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 11:57:06 2021

@author: rikushwa
"""

'''
Tip and Trick 1: How to measure the time elapsed to execute your code in Python
'''

import time

startTime = time.time()

# write your code or functions calls

endTime = time.time()
totalTime = endTime - startTime

print("Total time required to execute code is= ", totalTime)