#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 23:17:13 2021

@author: rita
"""
'''
x = [[4,5,6],[3,8,4]]
# xi=zip(*x)
# print(list(xi))

row=len(x)
col=len(x[0])
y=[]
z=[]
for i in range(col):
    y=[]
    for j in range(row):
        y.append(x[j][i])
    z.append(y)
print(z)
'''


'''
x = [[4,5,6,10],[11,3,8,4]]

n=[]
def cal(x):
    for i in range(len(x[0])):
       n.append([x[j][i] for j in range(len(x))])
    return n

print(cal(x))
'''


t = [[10,20],[30,40],[1,2]]
l=[]

for i in range(2):
    t1 = [lambda x=x: x[i] for x in t]
    t2 = [lambda x=x: x[i+1] for x in t]
    
for a in t:
    l.append(a())
    
for b in t1:
    l.append(b())
    
print(l)


