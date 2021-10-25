# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 20:31:27 2021

@author: rikushwa
"""

'''
Python Pandas
https://pynative.com/wp-content/uploads/2019/01/Automobile_data.csv

Exercise 1: From the given dataset print the first and last five row
'''

import pandas as pd
df = pd.read_csv(r'C:\Users\rikushwa\github\Python-Learning\Automobile_data.csv')
print(df.head(5))
print(df.tail(5))
