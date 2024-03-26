# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 12:22:42 2021

@author: rikushwa
"""

# importing pandas

import pandas as pd

# Creating Dictionary
d1 = {'id': [1, 2, 10, 12],
	'val1': ['a', 'b', 'c', 'd']}

a = pd.DataFrame(d1)

# Creating dictionary
d2 = {'id': [1, 2, 9, 8],
	'val1': ['p', 'q', 'r', 's']}
b = pd.DataFrame(d2)

print(a)
print()
print(b)

inner_join = pd.merge(a,b, on='id', how='inner')
print(inner_join)

left_outer_join = pd.merge(a, b, on='id', how='left')
print(left_outer_join)

right_outer_join = pd.merge(a, b, on='id', how='right')
print(right_outer_join)

full_outer_join = pd.merge(a, b, on='id', how='outer')
print(full_outer_join)

index_join = pd.merge(a, b, left_index=True, right_index=True)
print(index_join)

append_dfs = a.append(b)
print(append_dfs)

concats_dfs = pd.concat([a,b])
print(concats_dfs)

join_dfs = a.join(b)
print(join_dfs)

