## __iter__() - returns a iterator for given object
## Syntax:
## iter(object)
## iter(callable, sentinel)

l = [1,2,3,4,5,6,7,8,9]
it_l = iter(l)
print(next(it_l)) # 1
print(next(it_l)) # 2

print("Iterating using while loop")
while True:
    try:
        print(next(it_l))
    except StopIteration:
        break