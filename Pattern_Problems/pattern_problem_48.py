#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 15:00:50 2022

@author: rita
"""
'''
Pattern Problem - 48 (100 Marks)
You need to take an integer input and then draw the pattern according to it. Say for example if you enter 5 then, the pattern should be like this-
5 5 5 5 5 5 5 5 5
   4 4 4 4 4 4 4
      3 3 3 3 3
         2 2 2
            1 

Input Format
You will take an integer input n from stdin.

Constraints
1 <= n <= 1000

Output Format
Your output should be the pattern according to the input which you had entered. 

Sample TestCase 1
Input
5
Output
5 5 5 5 5 5 5 5 5
  4 4 4 4 4 4 4
    3 3 3 3 3
      2 2 2
        1

'''

def main():
    n = int(input())
    for i in range(n,-1,-1):
        if i !=0:
            sl=str(i)+" "
            sr=" "+str(i)
            s=str(i)
            res = str(sl*(i-1)).rjust((n-1)*2)+s+str(sr*(i-1)).ljust((n-1)*2)
            print(res.rstrip())
        
main()