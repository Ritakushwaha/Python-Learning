# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 17:29:47 2021

@author: rikushwa
"""

# NetworkError has base RuntimeError
# and not Exception
class Networkerror(RuntimeError):
	def __init__(self, arg):
		self.args = arg

try:
	raise Networkerror("Error")

except Networkerror as e:
	print (e.args)
