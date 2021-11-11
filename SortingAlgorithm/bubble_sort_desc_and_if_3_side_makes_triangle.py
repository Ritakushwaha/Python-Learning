# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 16:03:52 2021

@author: rikushwa
"""

from math import acos, pi

def bubble_sort_desc(arr):
    N = len(arr)
    for i in range(N-1):
        for j in range(0,N-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    a,b,c = arr[:3]
    ans = sss(a,b,c)
    return ans
    
def sss(a,b,c):
    a_angle = round(180/pi*acos((b**2+c**2-a**2)/(2*b*c)))
    b_angle = round(180/pi*acos((c**2+a**2-b**2)/(2*a*c)))
    c_angle = round(180/pi*acos((b**2+a**2-c**2)/(2*b*a)))
  
    if a_angle==0 or b_angle==0 or c_angle==0:
        return 0
    else:
        return a+b+c

if __name__ == '__main__':
    arr = [7,14,16]
    print(bubble_sort_desc(arr))