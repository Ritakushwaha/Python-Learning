# Inheritance

class Person(object):
    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name
    
    def isEmployee(self):
        return False

class Employee(object):
    def isEmployee(self):
        return True
    
class Per(Employee, Person):
    def __init__(self, name):
        super().__init__(name)
        print('Derived')


derived = Per('Rita')
print(derived.getName())

emp = Person('Rita')
print(emp.getName(), emp.isEmployee())
print(issubclass(Employee, Person))