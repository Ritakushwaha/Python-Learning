'''
yield - suspend's func. execution - sends a value - resume to send the next value
return - suspend's func. execution - sends a value to caller
'''

print('yield code block')
def gen():
    yield 1
    yield 2
    yield 3

for i in gen():
    print(i)

print('return code block')
def ret():
    return 1
    return 2  # NOT REACHABLE

print(ret())