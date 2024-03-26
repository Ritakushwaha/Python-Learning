#Generators - returns iterator using the yield keyword.

def gen():
    yield 1
    yield 2
    yield 3

for i in gen():
    print(i)


## Generator Expression
print('Generator Expression')
gen_exp = (i for i in range(5) if i%2==0)
for i in gen_exp:
    print(i)