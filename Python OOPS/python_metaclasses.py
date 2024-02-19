'''
Metaprogramming - we can say metaprogramming 
is the code that manipulates code.

Summary - Metaclass create Classes and 
            Classes creates objects

Example - using decorators
'''

# class Painting:
#     pass

# print(type(Painting)) # <class 'type'> # metaclass

# # obj = Painting()
# # print(type(obj)) # class is also an object

# # special clacc - type is default metaclass


## Custom Metaclass

class Painting:
    def fun(self):
        print("This is  a function from Painting")

# with type() we will create a metaclass
        
Art = type('Art', (Painting,), 
           {'fun': lambda self:print("This is a custom Art function")})
print(type(Art))
p1 = Art()
print(type(p1))
# print(p1.fun()) # This is a custom Art function
