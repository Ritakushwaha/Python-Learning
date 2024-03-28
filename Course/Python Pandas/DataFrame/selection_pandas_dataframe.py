import pandas as pd

df = pd.read_csv('.\Course\Python Pandas\Automobile_data.csv')

### Dealing with Columns
## Column Selection
selected_columns = df[['company', 'length']].head(5)
print("Selected columns ('company' and 'length') - Top 5 rows:\n", selected_columns)

## Column Addition
lst = list(range(len(df)))
df['index'] = lst
print("\nDataFrame with 'index' column added - Top 5 rows:\n", df.head(5))

## Column Deletion
df.drop(["horsepower"], axis=1, inplace=True)
print("\nDataFrame with 'horsepower' column deleted - Top 5 rows:\n", df.head(5))


### Dealing with Rows
## Row Selection
row_selection = df[(df['length'] > 50) & (df['price'] < 30000)]
print("Rows where 'length' > 50 and 'price' < 3000 - Top 5 rows:\n", row_selection.head())

# Setting the index to the 'company' column
df.set_index('company', inplace=True)

# Accessing the row with label 'alfa-romero'
print("\nRow with index label 'alfa-romero':\n", df.loc['alfa-romero'])

# Accessing the row with integer index 10
print("\nRow with integer index 10:\n", df.iloc[10])

# Accessing multiple rows with index [4:8]
print("\nRows with integer index [4:8]:\n", df.iloc[4:8])

## Row Addition
# Resetting the index to the default integer index
df.reset_index(inplace=True)

# Creating a new row of data
data = ['abc', 'sedan', 50.5, 100, 'ohc', 'two', None, 24000, 8]
new_rec = pd.DataFrame([data], columns=df.columns)

# Adding the new record to the DataFrame and resetting the index
df = pd.concat([new_rec, df]).reset_index(drop=True)
print("\nDataFrame after adding new record:\n", df.head())

## Row Deletion
df.drop(0, inplace=True)
print(df.head())


## Selecting two rows and three columns
df.set_index('company', inplace=True)
res = df.loc[["alfa-romero", "bmw"], 
                   ["body-style", "length", "price"]] 
print("\nSelecting two rows and three columns:\n", res)

## Selecting all of the rows and some columns
res = df.loc[:, ["body-style", "length"]]
print("\nSelecting all rows and two columns:\n", res)

## Selecting two rows and all columns using slicing
res = df.loc[["alfa-romero", "bmw"], :]
print("\nUsing slicing to select two rows and all columns:\n", res)

## Selecting two rows and two columns
res = df.iloc[[3, 4], [1, 2]]
print("Selected rows (3rd and 4th) and columns (2nd and 3rd):\n", res)