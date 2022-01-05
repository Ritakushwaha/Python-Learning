#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:26:55 2022

@author: rita
"""

def main(): 
    m=65
    for i in range(5):
        x = chr(m)
        print((x*i).rjust(5)+x+(x*i).ljust(5))
        m +=1
    print()
        
main()
    
