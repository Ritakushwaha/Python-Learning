import pandas as pd

df = pd.read_csv('.\Course\Python Pandas\Automobile_data.csv')

# Displaying the top 5 rows of the 'company' column
top = df['company'].head(5)
print("Top 5 companies:\n", top)

# Displaying the bottom 5 rows of the 'company' column
bottom = df['company'].tail(5)
print("\nBottom 5 companies:\n", bottom)

# Describing the 'company' column
description = df['company'].describe()
print("\nDescription of the 'company' column:\n", description)

# Selecting 'company' and 'length' columns
selection = df[['company', 'length']].head(5)

# Converting selection to a numpy array
arr = selection.to_numpy()
print("\nType of arr:", type(arr))
print("Array from 'company' and 'length' columns:\n", arr)

# Deprecated: Using as_matrix() to convert selection to a matrix (as_matrix() is deprecated)
# mat = selection.as_matrix()
# print("\nMatrix from 'company' and 'length' columns:\n", mat)
