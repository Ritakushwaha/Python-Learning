## Combinatoric iterators - recursive generators

#Product()
#Permutations()
#Combinations()
#Combinations_with_replacement()

from itertools import product, permutations, combinations, combinations_with_replacement

# cartesian product
print(list(product([1, 2], [3, 4])))
print(list(product('ABCD', 'xy')))
print(list(product([1,2], repeat=3)))

# permutations
print(list(permutations([1,'A'],2)))
print(list(permutations('AB')))
print(list(permutations(range(3),2)))

# combinations
print(list(combinations([1,2,3], 2))) # all possible
print(list(combinations('AB', 2))) 
print(list(combinations(range(3),2)))

# combinations_with_replacement() - gives result in sorted order
print(list(combinations_with_replacement(range(5), 3)))
print(list(combinations_with_replacement("ABC", 2)))
print(list(combinations_with_replacement(["a","b"], 2)))


