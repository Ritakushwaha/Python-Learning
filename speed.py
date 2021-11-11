# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 11:25:55 2021

@author: rikushwa
"""
import math

def solve(speed):
    v = math.sqrt(2*10*speed[0])-speed
    return v

N = int(input())

for i in range(0,N):
    speed = list(map(int, input().split()))

print(solve(speed))


    