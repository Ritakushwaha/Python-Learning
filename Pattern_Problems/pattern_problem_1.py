#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 22:01:50 2022

@author: rita
"""

'''
Pattern Problem - 1 (100 Marks)
You need to take an integer input and then draw the pattern according to it. 
Say for example if you enter 6 then, the pattern should be like this- 
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * * 

Input Format
You will take an integer input n from stdin.

Constraints
1 <= n <= 1000

Output Format
Your output should be the pattern according to the input which you had entered. 

Sample TestCase 1
Input
6
Output
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

    n = int(input())
    for i in range(n):
        for j in range(n-1):
            print('*',end=" ")
        print()

main()

