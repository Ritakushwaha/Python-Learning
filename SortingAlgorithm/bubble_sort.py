# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 12:37:56 2021

@author: rikushwa
"""

arr = [4,2,1,-1,7]

def bubbleSort(arr):
  n = len(arr)
 
  # Traverse through all array elements
  for i in range(n-1):
    for j in range(0, n-i-1): #last I elements are in place already
 
      # Swap if the element found is greater than the next element
      if arr[j]>arr[j+1] :
        arr[j], arr[j+1] = arr[j+1], arr[j]

bubbleSort(arr)
print("Sorted array: ", arr)