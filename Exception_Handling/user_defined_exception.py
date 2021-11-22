# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 17:14:52 2021

@author: rikushwa
"""

# A python program to create user-defined exception

# class MyError is derived from super class Exception
class MyError(Exception):

	# Constructor or Initializer
	def __init__(self, value):
		self.value = value

	# __str__ is to print() the value
	def __str__(self):
		return(repr(self.value)) #The repr() function returns the string representation of the value passed to eval function by default.

try:
	raise(MyError(3*2))
# Value of Exception is stored in error
except MyError as error:
	print('A New Exception occured: ',error.value)
