'''
First class functions - 
- instance of Object type.
- store a func in a variable
- pass the func as a parameter to another function
- store them in datastructures.
'''

# Functions are objects adn can be stored in variable:

def fun(a):
    return a.upper()

print(fun('daily_data_prep'))

f = fun
print(f('daily_data_prep'))

# Functions can be passed as argument to other functions
def fun1(a):
    return a.upper()

def fun2(b):
    return b.lower()

def fun3(f):
    print(f('This function accepts function as an argument'))


fun3(fun1)
fun3(fun2)


# Functions can return another function

def fun1(x):
    def fun2(y):
        return x+y
    
    return fun2

a = fun1(10)
b = a(20)
print(b)