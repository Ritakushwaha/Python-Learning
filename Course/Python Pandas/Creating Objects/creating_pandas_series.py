import pandas as pd

## Creating Empty Series
ser = pd.Series()
print(ser)


## Creating a series from array
import numpy as np
data = np.array(['daily', 'data', 'prep'])
ser = pd.Series(data)
print(ser)

## Creating a series from array with an index
data = np.array(['daily', 'data', 'prep'])
ser = pd.Series(data, index=['a','b','c'])
print(ser)

## Creating a series from Lists
lst = ['daily', 'data', 'prep']
ser = pd.Series(lst)
print(ser)

## Creating a series from Dictionary
dct = {'daily':1, 'data':2, 'prep':3}
ser = pd.Series(dct)
print(ser)

## Creating a series from Scalar value
ser = pd.Series(10, index=[0, 1, 2, 3, 4, 5])
print(ser)

## Creating a series using NumPy functions
# series with numpy linspace()
ser1 = pd.Series(np.linspace(3, 33, 3))
print(ser1)
 
# series with numpy linspace()
ser2 = pd.Series(np.random.randn(5))
print(ser2)

## Creating a Series using range function
ser=pd.Series(range(5))
print(ser)

## Creating a Series using for loop and list comprehension
ser=pd.Series(range(1,20,3), index=[x for x in 'abcdefg'])
print(ser)

## Creating a Series using mathematical expressions
ser=np.arange(10,15)
serobj=pd.Series(data=ser*5,index=ser)
print(serobj)