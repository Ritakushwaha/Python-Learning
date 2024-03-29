# importing pandas as pd
import pandas as pd

dict = {'name':["daily_data_prep", "enliven_arts", "seno.rita12"],
		'type': ["study", "art", "personal"]}
df = pd.DataFrame(dict, index = [True, True, False])
print(df)

## Accessing a DataFrame with a boolean index
# Accessing a Dataframe with a boolean index using .loc[]
print(df.loc[True])

# Accessing a Dataframe with a boolean index using .iloc[]
# print(df.iloc[True]) # TypeError: Cannot index by location index with a non-integer key
print(df.iloc[1])


## Applying a boolean mask to a dataframe
df = pd.DataFrame(dict, index = [0, 1, 2])
print(df[[True, False, True]])

## Masking data based on column value
print(df['type'] == 'personal')

## Masking data based on an index value
print(df[df.index==2])