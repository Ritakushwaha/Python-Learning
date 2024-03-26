'''
Static method - belong to a class but does not operate on the 
instance of that class. 
It can be called on an instance or on the class itself.

Define: @staticmethod decorator doesn't require self and cls parameter
'''

class Animal:
    @staticmethod
    def state_animal(arg1, arg2):
        return arg1,arg2
    
print(Animal.state_animal('Beer', 'Lion'))


