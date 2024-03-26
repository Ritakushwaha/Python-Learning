import pandas as pd

# Creating an Empty Series
empty_ser = pd.Series()
print("Empty Series:")
print(empty_ser)

# Creating a series from array
import numpy as np
data_array = np.array(['daily', 'data', 'prep'])
ser_array = pd.Series(data_array)
print("\nSeries from array:")
print(ser_array)

# Creating a series from array with an index
data_array_indexed = np.array(['daily', 'data', 'prep'])
ser_array_indexed = pd.Series(data_array_indexed, index=['a','b','c'])
print("\nSeries from array with index:")
print(ser_array_indexed)

# Creating a series from Lists
lst = ['daily', 'data', 'prep']
ser_lst = pd.Series(lst)
print("\nSeries from list:")
print(ser_lst)

# Creating a series from Dictionary
dct = {'daily':1, 'data':2, 'prep':3}
ser_dict = pd.Series(dct)
print("\nSeries from dictionary:")
print(ser_dict)

# Creating a series from Scalar value
ser_scalar = pd.Series(10, index=[0, 1, 2, 3, 4, 5])
print("\nSeries from scalar value:")
print(ser_scalar)

# Creating a series using NumPy functions
# Series with numpy linspace()
ser_linspace = pd.Series(np.linspace(3, 33, 3))
print("\nSeries using numpy linspace():")
print(ser_linspace)

# Series with numpy random.randn()
ser_randn = pd.Series(np.random.randn(5))
print("\nSeries using numpy random.randn():")
print(ser_randn)

# Creating a Series using range function
ser_range = pd.Series(range(5))
print("\nSeries using range function:")
print(ser_range)

# Creating a Series using for loop and list comprehension
ser_list_comp = pd.Series(range(1,20,3), index=[x for x in 'abcdefg'])
print("\nSeries using list comprehension:")
print(ser_list_comp)

# Creating a Series using mathematical expressions
ser_math_expr = np.arange(10,15)
ser_math_expr_obj = pd.Series(data=ser_math_expr*5,index=ser_math_expr)
print("\nSeries using mathematical expressions:")
print(ser_math_expr_obj)
