# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:32:28 2021

@author: rikushwa
"""
'''
A simple approach is to do linear search, i.e

Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
If x matches with an element, return the index.
If x doesn’t match with any of elements, return -1.
'''
# Searching an element in a list/array in python
# can be simply done using \'in\' operator
# Example:
# if x in arr:
# print arr.index(x)

# If you want to implement Linear Search in python

# Linearly search x in arr[]
# If x is present then return its location
# else return -1

def search(arr, x):

	for i in range(len(arr)):

		if arr[i] == x:
			return i

	return -1

arr = [20,21,2,3,4,22,23,24]
x = arr[7]
print(search(arr,x))