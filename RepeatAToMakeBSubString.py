'''
Input:
A = "abcd"
B = "cdabcdab"
Output:
3
Explanation:
Repeating A three times (“abcdabcdabcd”),
B is a substring of it. B is not a substring
of A when it is repeated less than 3 times.
Example 2:
Input:
A = "ab"
B = "cab"
Output :
-1
Explanation:
No matter how many times we repeat A, we can't
get a string such that B is a substring of it.



Constraints:
1 ≤ |A|, |B| ≤ 103
String A and B consists of lower case alphabets

'''

def repeat_A_to_make_B_substring(A, B):
    count = 1
    a=A
    while len(A) <= len(B):
        A += a
        count+=1
    else:
        if B in A:
            return count
        else:
            return -1
    
if __name__ == '__main__':
    A = input()
    B = input()
    print(repeat_A_to_make_B_substring(A,B))