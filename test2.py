# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 10:49:55 2021

@author: rikushwa
"""

def mul(f):
    def cal(*args, **kwargs):
        result = f(*args, **kwargs)
        return result
    return cal

@mul
def mul(a,b):
    return a*b
print(mul(3,b=6))