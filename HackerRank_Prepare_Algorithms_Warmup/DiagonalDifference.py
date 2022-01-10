#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 17:30:12 2022

@author: rita
"""
'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

Function description

Complete the  function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers
Return

int: the absolute diagonal difference
Input Format

The first line contains a single integer, , the number of rows and columns in the square matrix .
Each of the next  lines describes a row, , and consists of  space-separated integers .

Constraints

Output Format

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

Sample Input

3
11 2 4
4 5 6
10 8 -12
Sample Output

15
Explanation

The primary diagonal is:

11
   5
     -12
Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:

     4
   5
10
Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15

Note: |x| is the absolute value of x
'''

def diagonalDifference(arr,n):
    d1 = 0
    d2 = 0
    for i in range(n):
        for j in range(n):
            if i==j:
                d1 +=arr[i][j]

    j = n-1
    for i in range(n):
        d2 +=arr[i][j]
        j-=1
    
    return (abs(d1-d2))
    
if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
            arr.append(list(map(int,input().split())))

    print(diagonalDifference(arr,n))