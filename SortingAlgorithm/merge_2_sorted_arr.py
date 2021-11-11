# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 13:49:29 2021

@author: rikushwa
"""

def merge(a1, a2, p1, p2):
  temp = []
  
  while p1< len(a1) and p2<len(a2):
    if a1[p1]<a2[p2]:
      temp.append(a1[p1])
      p1 += 1
    else:
      temp.append(a2[p2])
      p2 += 1
      
  if p2 == len(a2):
    temp.extend(a1[p1:])
  elif p1 == len(a1):
    temp.extend(a2[p2:])
      
  return temp
    

a1 = [1,2,10,11,7,12,16,19,20,23]
a2 = [4,6,8,9,13]
p1=0
p2=0
print(merge(a1,a2,p1,p2))