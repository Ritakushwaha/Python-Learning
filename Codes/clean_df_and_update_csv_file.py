# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 20:40:54 2021

@author: rikushwa
"""

'''
Python pandas
Exercise 2: Clean the dataset and update the CSV file
'''

import pandas as pd
df = pd.read_csv(r'C:\Users\rikushwa\github\Python-Learning\Automobile_data.csv',na_values={
'price':["?","n.a"],
'stroke':["?","n.a"],
'horsepower':["?","n.a"],
'peak-rpm':["?","n.a"],
'average-mileage':["?","n.a"]})
print(df)

df.to_csv(r'C:\Users\rikushwa\github\Python-Learning\Automobile_data.csv')
