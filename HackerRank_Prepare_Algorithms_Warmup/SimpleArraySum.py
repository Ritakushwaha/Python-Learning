#!/bin/python3

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    return sum(ar)

if __name__ == '__main__':
    ar = list(map(int,input().split()))
    result = simpleArraySum(ar)
    print(result)
