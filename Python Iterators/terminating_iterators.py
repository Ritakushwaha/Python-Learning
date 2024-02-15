# Terminating Iterators

import itertools
import operator

## accumulate(iter, func)
l = [2,3,4,5,6]
print(list(itertools.accumulate(l))) # by default addition performed
print(list(itertools.accumulate(l, operator.mul)))  # multiplication
print(list(itertools.accumulate(l, lambda x, y: x**y)))   # power function


## chain(iter1, iter2)
l = [1,2,3]
l1 = [4,5,6]
print(list(itertools.chain(l, l1)))    # concatenates two lists

## chain.from_iterable() 
d = {'a':[1,2,3,5,6,7], 'b':[3,4]}
print(list(itertools.chain.from_iterable(d.values())), end=" ")     # flattening the dictionary values into a single list

## compress(iter, selector)
s = "abcadefg"
print(list(itertools.compress(s, [1,0,0,1,0,1,0,1]))) # 1 is true

## dropwhile(func, seq)
l = [2, 4, 5, 7, 8]
print(list(itertools.dropwhile(lambda x : x < 3 , l)))
print (list(itertools.dropwhile(lambda x : x % 2 == 0, l)))

## filterfalse(func, seq)
l = [2, 4, 5, 7, 8]
print(list(itertools.filterfalse(lambda x : x % 2 == 0, l)))

## islice(iterable, start, stop, step)
l = list(range(9))
print(list(itertools.islice(l, 2, None, 2)))

## starmap(func, tuple list)
l = [(1, 10), (8, 1), (5, 9), (11, 1)]
print(list(itertools.starmap(operator.add, l)))

## takewhile(func, iterable)
l = [2, 4, 5, 7, 8, 2]
print(list(itertools.takewhile(lambda x : x < 7 , l)))

## tee(iterator, count)
l = [2, 4, 5, 7, 8, 2]
iti = iter(l)
it = itertools.tee(iti, 10)
for i in range(len(it)):
    print(list(it[i]))

# zip_longest( iterable1, iterable2, fillval)
fruit = ['apple', 'banana', 'orange']
print(*(itertools.zip_longest(fruit, 'abcd', '_')))