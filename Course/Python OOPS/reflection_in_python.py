# Reflection - ability for code to be able to examine attributes about objects that might be passed a sparameters to a fuction.
# Reflection enabling functions:
    ## type and isinstance
    ## Callable() - if obj callable - return True
    ## Dir - dir() - return a list of valid attributes of obj
    ## Getattr - getattr() retrun the value of the named attributes

def reverse(sequence):
    sequence_type = type(sequence) #list
    empty_sequence = sequence_type() #[]

    print(sequence_type,empty_sequence)

    if sequence == empty_sequence:
        return empty_sequence
    
    rest = reverse(sequence[1:])
    first_sequence = sequence[0:1]
    print(rest,first_sequence)

    final_result = rest+first_sequence
    print(final_result)
    return final_result

print(reverse([1,2,3])) # [3,2,1]
# print(reverse("hello")) # "olleh"