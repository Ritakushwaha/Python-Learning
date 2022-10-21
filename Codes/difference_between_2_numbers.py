''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    a = int(input())
    b = int(input())

    if a>b:
        c = a-b
    c = b-a

    print(c)

main()