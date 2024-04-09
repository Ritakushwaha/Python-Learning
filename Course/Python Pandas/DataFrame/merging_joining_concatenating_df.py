### Adding new column to existing DataFrame in Pandas

import pandas as pd

data = {'Name': ['Ritu', 'Rita', 'Ritte', 'Ritz'],
		'Qualification': ['BE', 'BTECH', 'NIFT', 'MBA']}
df = pd.DataFrame(data)
print(df)

## By using Dataframe.insert() method
df.insert(2, "Age", [21, 23, 24, 21], True)
print(df)

# By using Dataframe.assign() method
df2 = df.assign(address=['Delhi', 'Bangalore', 'Chennai', 'Patna'])
print(df2)

# Using Dictionary
addd = {'Address':['ABC', 'Bangalore', 'Chennai', 'Patna']}
df['Address'] = addd
# Using List
# Using .loc() 
# Adding More than One columns in Existing Dataframe 