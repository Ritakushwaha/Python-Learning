# Infinite iterators 

import itertools
# count(start,step)
for i in itertools.count(2,2):
    if(i>=55):
        break
    else:
        print(i, end=" ")

#cycle(iterable)
for i in itertools.cycle([0,1,2,3,4,5,6,7]):
    if i>6 :
        break
    print(i, end=" ")

# repeat(val, num)
print(list(itertools.repeat("a", 10)))
print(list(itertools.repeat("abcds", 2)))

# next(iterator)
l = [1,2,3,4,5]

it=itertools.cycle(l)
for i in range(9):
    print(next(it),end=' ')
