'''
A pandas DataFrame is a two-dimensional, size-mutable, and heterogeneous tabular data structure with labeled axes (rows and columns), similar to a spreadsheet or SQL table. It is a fundamental tool in Python for data manipulation and analysis, particularly in the realm of data science and machine learning.

Here are some key characteristics of a pandas DataFrame:

Tabular Structure: Data is organized in rows and columns, where each column can have a different data type (integer, float, string, etc.).

Labeled Axes: Both rows and columns have labels, which allow for easy indexing and manipulation of data.

Size Mutability: You can modify the size (number of rows and columns) of a DataFrame after it has been created.

Data Alignment: Data is automatically aligned along the row and column labels when performing operations, making it easy to work with incomplete or misaligned data.

Rich Functionality: Pandas provides a wide range of functions and methods for data manipulation, cleaning, aggregation, reshaping, and analysis.
'''

## Create a pandas DataFrame:

import numpy as np
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

# Create a DataFrame from the dictionary of ndarray/list
df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# Missing data
data2 = {'Name': ['Alice', 'Bob', np.nan, 'David'],
        'Age': [25, np.nan, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', np.nan]}
df2 = pd.DataFrame(data2)

# Check for missing values
print("\nMissing values in df2:")
print(df2.isnull())

# Fill missing values
df3 = df2.fillna('UNKNOWN')
print("\nDataFrame with missing values filled:")
print(df3)

# Dropping missing values
df4 = df2.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df4)

## Iterating over rows
print("\nIterating over rows in df:")
for index, row in df.iterrows():
    print("Index:", index)
    print("Row:", row)
    print()


## Iterating over Columns
columns = list(df)
print("\nIterating over columns in df:")
for column in df:
    print("Column:", column)
    print("Value at index 2:", df[column][2])
