import pandas as pd

df = pd.read_csv('.\Course\Python Pandas\Automobile_data.csv')

# Displaying the top 5 rows of the DataFrame
data_top = df.head()
print("Top 5 rows of the DataFrame:\n", data_top)

# Describing the DataFrame
description = df.describe()
print("\nDescription of the DataFrame:\n", description)

# Converting the top 5 rows to a numpy array
arr = data_top.to_numpy()
print("\nType of arr:", type(arr))
print("Array representation of the top 5 rows:\n", arr)
