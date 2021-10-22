# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 17:44:34 2021

@author: rikushwa
"""

'''
Python Data Structure:
    Exercise 3: Slice list into 3 equal chunks and reverse each chunk
'''

l = [11, 45, 8, 23, 14, 12, 78, 45, 89, 100, 11, 12, 1, 2, 3]

def divide_list_in_equal_chunk_and_reverse(l):
    chunk_size = int(len(l)/3)
    start = 0
    end = chunk_size
    
    for i in range(3):
        chunk = l[start:end]
        print(list(reversed(chunk)))
        
        start = end
        end += chunk_size
    
divide_list_in_equal_chunk_and_reverse(l)
    