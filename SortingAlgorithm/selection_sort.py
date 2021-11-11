# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 08:18:02 2021

@author: rikushwa
"""

def selection_sort(arr):
    N = len(arr)
    for i in range(0,N-1):
    	for j in range(i+1, N):
    		if arr[j] < arr[i]:
    		    arr[i], arr[j] = arr[j],arr[i]
    return arr

arr = [3,4,5,6,5,2,3,2,1]
print(selection_sort(arr))