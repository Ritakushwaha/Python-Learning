# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 20:52:25 2021

@author: rikushwa
"""

'''
Python Pandas

Exercise 3: Find the most expensive car company name
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

print(max(df['price']))

df = df [['company','price']][df.price==df['price'].max()]

print(df)

'''
Exercise 4: Print All Toyota Cars details
'''

car_Manufacturers = df.groupby('company')
#toyotaDf = car_Manufacturers.get_group('toyota')
print(car_Manufacturers)