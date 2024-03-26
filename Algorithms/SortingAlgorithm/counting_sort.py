# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 13:16:08 2021

@author: rikushwa
"""

def countingSort(arr):
  # create additional array [0, max(arr)+1]
  counts = [0 for _ in range(max(arr)+1)]
        	
  for val in arr: # forming counts array
    counts[val]+=1
                
  arr = [] # clear array
  for key, count in enumerate(counts):
    while count>0:
      arr.append(key)
      count -= 1
  
  return arr
      
arr = [0,2,3,1,3,2]
print(countingSort(arr))