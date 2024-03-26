# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 12:56:23 2021

@author: rikushwa
"""

def merge(arr, m):
  i, j = 0, m # pointers at the beginnings of subarrays
  temp = []
        	
   # merge sorted arrays to temp
  while i<m or j<len(arr):
    if i>=m:
      temp.append(arr[j])
      j+=1
    elif j>=len(arr):
      temp.append(arr[i])
      i+=1
    else:
      if arr[i] < arr[j]:
        temp.append(arr[i])
        i+=1
      else:
        temp.append(arr[j])
        j+=1
  return temp
    	
def mergeSort(arr):
  if len(arr) == 1: # base case
    return arr
  m = len(arr) // 2
 
  arr[:m] = mergeSort(arr[:m])
  arr[m:] = mergeSort(arr[m:])
  return merge(arr, m)

arr = [6,4,3,2,5,1]
n =len(arr)
print(mergeSort(arr))