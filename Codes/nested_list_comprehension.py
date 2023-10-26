# Nested list comprehension 
matrix = [[j for j in range(2)] for i in range(3)] 
  
print(matrix)

flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)