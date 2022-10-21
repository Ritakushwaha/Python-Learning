# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 13:23:49 2021

@author: rikushwa
"""

"""
Given an array of integers nums sorted in non-decreasing order, find the starting position of a given target value.

If target is not found in the array, return -1.
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: 3

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: -1

Example 3:

Input: nums = [], target = 0
Output: -1

"""

# Python3 Program for recursive binary search.

# Returns index of x in arr if present, else -1
value =[-1]

def binarySearch(arr, l, r, x):
  if r >= l:
    mid = l + (r - l)//2
    if arr[mid] == x:
      value.append(mid)
      return binarySearch(arr,l,mid-1,x)
    elif arr[mid] > x:
      return binarySearch(arr, l, mid-1, x)
    else:
      return binarySearch(arr, mid + 1, r, x)
  else:
    return -1

# Function cal

def find_target(arr,target):
  low = 0
  high = len(arr)
  binarySearch(arr,low,high,target)
  print(value[-1])

target = 6
arr = [5,7,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,10]
find_target(arr,target)



#Produce a list of facilities with more than 1000 slots booked. Produce an output table consisting of facility id and slots, sorted by facility id.

'''select f.facid, sum(slots) as total_slots 
from cd.facilities f inner join cd.bookings b on f.facid = b.facid
group by f.facid having sum(slots)>1000 
order by f.facid;'''




l=['12','34','5']
print(len(list(list(list(map(list,l))))))