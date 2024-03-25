'''
Series :  one-dimensional array-like object that can hold any data type, such as integers, floats, strings, Python objects, etc. It is similar to a one-dimensional array or list but with additional functionalities and capabilities.
A pandas Series consists of two main components:

Data: This can be any data type, such as integers, floats, strings, Python objects, etc. Each element in the Series has a corresponding index, which is used to access and manipulate the data.

Index: This is a sequence of labels that uniquely identifies each element in the Series. The index can be integers, strings, or any other data type that can be used as labels.
'''

# Create a Python Pandas Series
import pandas as pd

# Creating a Series from a list
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

print(series)