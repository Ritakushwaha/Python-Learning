# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 17:42:29 2021

@author: rikushwa
"""
'''
#lookup Error (Index Error,Key Error    )
try:
	a = [1, 2, 3]
	print (a[3])
except LookupError:
	print ("Index out of bound error.")
else:
	print ("Success")

#Attribute Error

class Attributes(object):
	pass

object = Attributes()
print (object.attribute)

# Airthmetic Error
try:
	a = 10/0
	print (a)
except ArithmeticError:
		print ("This statement is raising an arithmetic exception.")
else:
	print ("Success.")'''
    
'''
#EOF Error
while True:
	data = input('Enter name : ')
	print ('Hello ', data)
    
#ORDER FLOW ERROR
import math

print (math.exp(1000)) 

#Generator Error
def my_generator():
	try:
		for i in range(5):
			print ('Yielding', i)
			yield i
	except GeneratorExit:
		print ('Exiting early')

g = my_generator()
print (g.next())
g.close()'''

'''
import sys

print ('Regular integer: (maxint=%s)' % sys.maxint)
try:
	i = sys.maxint * 3
	print ('No overflow for ', type(i), 'i =', i)
except OverflowError, err:
	print ('Overflowed at ', i, err)

print()
print ('Long integer:')
for i in range(0, 100, 10):
	print ('%2d' % i, 2L ** i)

print()
print ('Floating point values:')
try:
	f = 2.0**i
	for i in range(100):
		print (i, f)
		f = f ** 2
except OverflowError, err:
	print ('Overflowed after ', f, err)'''
    
import gc
import weakref

class Foo(object):

	def __init__(self, name):
		self.name = name
	
	def __del__(self):
		print ('(Deleting %s)' % self)

obj = Foo('obj')
p = weakref.proxy(obj)

print ('BEFORE:', p.name)
obj = None
print ('AFTER:', p.name)








