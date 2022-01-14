#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 15:18:17 2022

@author: rita
"""

'''
Pattern Problem - 33 (100 Marks)
You need to take an integer input and then draw the pattern according to it. Say for example if you enter 5 then, the pattern should be like this-

A B C D E
   A B C D
      A B C
         A B
            A 

Input Format
You will take an integer input n from stdin.

Constraints
1 <= n <= 26

Output Format
Your output should be the pattern according to the input which you had entered. 

Sample TestCase 1
Input
5
Output
A B C D E
  A B C D
    A B C
      A B
        A
        
'''
def main():

    n = int(input())
    
    for i in range(n):
        c = 65
        res=""
        for j in range(i,n):
            res += chr(c)+" "
            c+=1
        print(res.rjust(n*2))

main()