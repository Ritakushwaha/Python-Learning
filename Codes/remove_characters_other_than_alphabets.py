# Python code to remove all characters 
# other than alphabets from string 

input = "$ILove*R;i..ta, so'Mu^ch?"

sepChars = [char for char in input if ord(char) in range(ord('a'),ord('z')+1) or ord(char) in range(ord('A'),ord('Z')+1)] 
print(sepChars)

word = ''.join(sepChars) 
print(word) 
