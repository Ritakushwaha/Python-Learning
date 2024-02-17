# We can return multipple values from a function.

'''
1. Using Object
2. Using Tuple
3. Using List
4. Using Dictionary
5. Using Data Class
6. Using yield
'''

# 1. Using Object
class Test:
    def __init__(self):
        self.channel = 'daily_data_prep'
        self.platform1 = 'instagram'
        self.platform2 = 'youtube'

def fun():
    return Test()

print(fun().channel, fun().platform1, fun().platform2)
print(Test().channel, Test().platform1, Test().platform2)


# 2. Using Tuple
def func():
    return 'Hello', 'daily_data_prep'

print(func()) # ('Hello', 'daily_data_prep') - a tuple



# 3. Using List
def func1():
    return ['Hello', 'daily_data_prep']

print(func1()) # ['Hello', 'daily_data_prep'] - a list
print(func1()[1])
print(func1()[0])


# 4. Using Dictionary
def func2():
    return {'channel': 'daily_data_prep', 'platform1':'instagram', 'platform2':'youtube'}

print(func2()) # {'channel': 'daily_data_prep', 'platform1': 'instagram', 'platform2': 'youtube'} - a dictionary
print(func2()['platform1'])
print(func2()['platform2'])
print(func2()['channel'])


# 5. Using Data Class (Python3.7+)

from dataclasses import dataclass

@dataclass
class Painting:
    name: str
    cost: float

painting = Painting('Beauty with brain', 2500)
print(painting)
print(painting.cost)


# 6. Using yield

def gen():
    yield 'daily_data_prep'
    yield ['instagram', 'youtube']

res = gen()
print(next(res))
print(next(res))

