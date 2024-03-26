# Function Decorators - 

def decorate_msg(fun):
    def addGreeting(person_name):
        return 'Welcome to '+fun(person_name)
    return addGreeting

@decorate_msg
def person(person_name):
    return person_name

print(person('Rita'))