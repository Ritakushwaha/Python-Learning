'''
Partial Functions - to fix certain number of arguments of a func and
generate new function
'''

from functools import partial
def fun(a,b,c,x):
    return 2*a + b*c + x*a

part = partial(fun, 3,1,4)

print(part(5))