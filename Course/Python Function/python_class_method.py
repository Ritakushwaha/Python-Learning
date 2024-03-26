# Class method - belong to class itself
# Define - @classmethod decorator
# first parameter of class method is - class itself (cls)
# useful for modifying and accessing class level attributes

class  Animal:
    def __init__(self, name, state):
        self.name = name
        self.state = state

    @classmethod
    def state_animal(cls, name, state):
        return cls(name, state)
    
animal1 = Animal('Tiger', 'MP')
animal2 = Animal('Swamp deer', 'UP')
    
print(animal1.name, animal1.state)
print(animal2.name, animal2.state)