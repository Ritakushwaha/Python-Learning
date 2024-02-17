'''
Memoization - technique of recording intermediate 
results so that it can avoid repeated calculation and
speed up program

Mostly useful in  - recursive programs
'''

memory = {}

def memoize_factorial(func):
    def inner(num):
        if num not in memory:
            memory[num] = func(num)
            print('result saved in memory')
        else:
            print('result from saved memory')
        return memory[num]
    return inner

@memoize_factorial
def facto(num):
    if num == 1:
        return 1
    else: 
        return num * facto(num-1)

print(facto(5))
print(facto(1))
print(facto(2))
print(facto(3))
print(facto(5))

