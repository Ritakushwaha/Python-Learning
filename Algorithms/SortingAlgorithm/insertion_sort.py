# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 12:41:54 2021

@author: rikushwa
"""

def insertionSort(arr):
  # traverse unsorted subarray
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1

  # traverse sorted part and replace elements one position right
    while j>=0 and key < arr[j]: 
      arr[j+1] = arr[j]
      j-=1

    # put key element on its position
    arr[j+1]= key
    
  return arr
    
arr=[2,4,3,5,6]
print(insertionSort(arr))