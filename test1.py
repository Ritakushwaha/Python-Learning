# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 10:39:13 2021

@author: rikushwa
"""

def main(sample_list):
    def compute():
        return sum([i for i in sample_list if isinstance(i, float)])
    result = compute()
    final_list.append(result)
    return final_list
sample_list = [1000,1010.90,3450,7809.23]
final_list=[]
print(main(final_list))