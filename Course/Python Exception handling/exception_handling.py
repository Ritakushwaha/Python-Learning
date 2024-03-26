'''
Errors-
1. Syntax Error: invalid syntax 
2. Exceptions: 
    Syntax Error
    TypeError
    NameError
    IndexError
    KeyError
    ValueError
    AttributeError
    IOError
    RuntimeError
    ZeroDivisionError
    ImportError
'''

### Examples - 
'''## Syntax Error
x = 4
if(x<5) #SyntaxError: expected ':'
print(f"{x} is less than 5")

## ZeroDivisionError
a =10
b = a/0 #ZeroDivisionError: division by zero
print(b)

## TypeError
x = 5
y = 'Rita'
z = x+y # TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''
## use try except block to handle the exception
x = 5
y = 6
try:
    z= x+y
    if z>10:
        raise ValueError("Sum of numbers is greater than 10")
except ValueError:
    print('Value Error')
except TypeError:
    print('Cannot add integer and string')
else:
    print("Addition of",x,"and",y,"is",z)
finally:
    print("This is finally block")