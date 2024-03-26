## Use of finally for cleanup
def divide(x,y):
    try:
        result = x//y
    except ZeroDivisionError:
        print(f"Error! Cannot divide by zero. You tried to divide {x} by 0.")
    else:
        print(f"The division of {x} by {y} is {result}.")
    finally:
        print(f"\nExecution completed.\n")

divide(10,0)