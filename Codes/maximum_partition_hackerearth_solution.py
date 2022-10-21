# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 11:07:36 2021

@author: rikushwa
"""

'''
Problem
There is an array of N integers, you are given a task to make any number of partitions in the array such that the Special Sum of all the partitions combined is maximized.

Suppose you make K partitions then the Special Sum is defined as P1 - P2 + P3 - P4 + P5 ..... +(-1)(K - 1)Pk.

Here Pi is defined as summation of all integers in that partition.

Input :

  The first line of input consist of an integer N, which denotes the number of integers in the array.    
  The second line of input consist of N integers, which denotes the values of the array.
Output :

 A single integer which denotes the maximum value of the Special Sum that can be obtained by any number of partitions.
Constraint :

Sample Input
5
1 -2 -3 2 1
Sample Output
9
Time Limit: 1
Memory Limit: 256
Source Limit:
Explanation
You can make three partitions , first from [0,0], second from [1,2] and third from [3,4].

Special value of such partions = 1 - (-2 + -3) + (2 + 1) = 9.
'''       

def solve(N,A):

    dp=[0]*N

    dp[0]=A[0]

    for i in range(1,N):

        dp[i]=max(dp[i-1]+A[i],dp[i-1]-A[i])

    return dp[N-1]

N=int(input())

A=list(map(int,input().split()))

out_=solve(N,A)

print(out_)