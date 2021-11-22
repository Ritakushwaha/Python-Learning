# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 17:06:32 2021

@author: rikushwa
"""

# Program to depict Raising Exception

try:
	raise NameError("Hi there") # Raise Error
except NameError:
	print ("An exception")
	raise # To determine whether the exception was raised or not
