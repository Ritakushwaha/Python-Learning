#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 18:07:40 2021

@author: rita
"""
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    a=int(input())
    b=int(input())
    if a>b:
        c = a//b
    else:
        c = b//a
    
    print(c)

main()

