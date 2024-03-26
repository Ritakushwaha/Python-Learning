import pandas as pd

## Creating Empty DataFrame
# Calling DataFrame constructor
df = pd.DataFrame()
print("Empty DataFrame:")
print(df)


## Creating a dataframe using List
lst = ['daily', 'data', 'prep']
# Calling DataFrame constructor on list
print("\nDataFrame from list:")
print(df)

## Creating DataFrame from dict of ndarray/lists
# initialise data of lists.
data = {'Name':['Rita', 'Ritu'], 'Age':[20, 21]}
df = pd.DataFrame(data)
print("\nDataFrame from dict of ndarray/lists:")
print(df)

#or
print("\nDataFrame from lists using dictionary:")
df = pd.DataFrame.from_dict(data)
print(df)

## Create pandas dataframe from lists using dictionary
# dictionary of lists
dict = {'name':["Rita", "Ritu"],
        'degree': ["BE", "BTech"],
        'score':[90, 40]}
df = pd.DataFrame(dict)
print("\nDataFrame from Lists using Dictionaries:")
print(df)

## Create DataFrame from lists of lists
# initialize list of lists
data = [['Rita', 10], ['Ritu', 15], ['Ritte', 14]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print("\nDataFrame from a lists of list:")
print(df)

## Create DataFrame from List of Dictionaries
# Initialize data to lists.
data = [{'a': 1, 'b': 2, 'c': 3},
        {'a': 10, 'b': 20, 'c': 30}]
df = pd.DataFrame(data)
print("\nDataFrame from List of Dictionaries:")
print(df)

#or

# Initialize data of lists
data = [{'b': 2, 'c': 3}, {'a': 10, 'b': 20, 'c': 30}]
df = pd.DataFrame(data, index=['first', 'second'])
print("\nDataFrame from List of Dictionaries with Index:")
print(df)

## Create DataFrame from a dictionary of Series
# Initialize data to Dicts of series.
d = {'one': pd.Series([10, 20, 30, 40],
                      index=['a', 'c', 'd', 'e']),
     'two': pd.Series([10, 20, 30, 40],
                      index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print("\nDataFrame from a dictionary of Series:")
print(df)

## Create DataFrame using the zip() function
name = ['rita', 'ritu', 'ritte']
age = [25, 30, 26]
data =  list(zip(name, age))
df = pd.DataFrame(list(data), columns=['name','age'])
print("\nDataFrame using the zip() function:")
print(df)

## Create a DataFrame by proving the index label explicitly
# initialize data of lists.
data = {'Name': ['Tom', 'Jack', 'nick', 'juli'],
        'Marks': [99, 98, 95, 90]}
df = pd.DataFrame(data, index=['rank1',
                               'rank2',
                               'rank3',
                               'rank4'])
print("\nDataFrame with explicit index label:")
print(df)

## Create DataFrame from List by changing data type
lst = [['Ritu', 'Kush', 25], ['Rita', 'Kushwaha', 30],
       ['Ritte', 'Kushwa', 26], ['Ritz', 'Kus', 22]]
   
df = pd.DataFrame(lst, columns =['FName', 'LName', 'Age'])
df['Age'] = df['Age'].astype(float)
print("\nDataFrame from List by changing data type:")
print(df)

#or

# Define column names and their data types in a dictionary
columns = {'FName': str, 'LName': str, 'Age': float}
# Create DataFrame using the dictionary of columns
df = pd.DataFrame(lst, columns=columns.keys()).astype(columns)
print("\nDataFrame from List by changing data type:")
print(df)

#or

df = df.applymap(lambda x: float(x) if isinstance(x, int) else x)
print("\nDataFrame from List by changing data type:")
print(df)

#or

df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
print("\nDataFrame from List by changing data type:")
print(df)


## Create DataFrame from List with index and column names
lst = ['daily', 'data', 'prep']
df = pd.DataFrame(lst, index =['a', 'b', 'c'],
                                              columns =['Names'])
print("\nDataFrame from List with index and column names:")
print(df)