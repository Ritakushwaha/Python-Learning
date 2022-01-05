#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 19:33:19 2022

@author: rita
"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
    
'''
Pattern Problem - 3 (100 Marks)
You need to take an integer input and then draw the pattern according to it. Say for example if you enter 5 then, the pattern should be like this-
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

Input Format
You will take an integer input  n from stdin.

Constraints
1 < = n < = 1000

Output Format
Your output should be the pattern according to the input which you had entered. 

Sample TestCase 1
Input
5
Output
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''

def main():
    n = int(input())

    for i in range(n):
        for j in range(n):
            print(j+1,end=" ")
        print()

main()