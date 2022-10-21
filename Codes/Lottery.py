# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 11:45:25 2021

@author: rikushwa
"""

def solve(A, B):
    
    n = len(B)
    count = 0 
    
    for i in range(0,n-1):
        for j in range(0, n-i-1):
            if B[j]>B[j+1]:
                B[j],B[j+1]=B[j+1],B[j]
                count+=1
    return count
    
    
A = int(input())
B = list(map(int,input().strip().split()))[:A]

print(B)
a = solve(A,B)
print(a)