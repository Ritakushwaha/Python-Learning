'''
Series :  one-dimensional array-like object that can hold any data type, such as integers, floats, strings, Python objects, etc. It is similar to a one-dimensional array or list but with additional functionalities and capabilities.
A pandas Series consists of two main components:

Data: This can be any data type, such as integers, floats, strings, Python objects, etc. Each element in the Series has a corresponding index, which is used to access and manipulate the data.

Index: This is a sequence of labels that uniquely identifies each element in the Series. The index can be integers, strings, or any other data type that can be used as labels.
'''

import pandas as pd

## Creating a Series from a list
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print("Series:")
print(series)

## Accessing Element from Series with Position
# The position starts at zero for the first element in the series.
value_at_position_zero = series [0]
print("\nValue at position zero:")
print(value_at_position_zero)

## Accessing Elements using Label based Indexing
series = pd.Series(data, index=['A','B','C','D','E'])
value_at_label = series['C']
print("\nValue at label 'C':")
print(value_at_label)

## Slicing a Series
slice_of_series = series[3:len(series)]
print("\nSlice of series:")
print(slice_of_series)

## Stepping through a Series
step_through_series = series[::2] # This will return every second element starting from index 0. # It is equivalent to series[0:len(series):2].
print("\nStepped through series:")
print(step_through_series)

## Indexing a Series using indexing operator []
print("\nIndexing using indexing operator []:")
print(series[3:6])

## Indexing a Series using .loc[ ]
print("\nIndexing using .loc[]:")
print(series.loc['C']) #provide label

## Indexing a Series using .iloc[ ]
print("\nIndexing using .iloc[]:")
print(series[2:4])

## Binary Operation on Series
data = pd.Series([5, 2, 3,7], index=['a', 'b', 'c', 'd'])
data1 = pd.Series([1, 6, 4, 9], index=['a', 'b', 'd', 'e'])
# add two series using .add() function
res = data.add(data1, fill_value=0)
print("Result of addition:")
print(res)
# subtract two series using .sub() function
diff = data.sub(data1)
print("\nResult of subtraction:")
print(diff)

