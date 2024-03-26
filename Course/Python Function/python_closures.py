'''
Python Closures: function object that remembers values
in enclosing scopes even if they are not present in memory
- used as a callback function, datahiding
'''

# Nested function and non local variable

def fun(a):
    def inner_fun():
        print(a)
    return inner_fun

if __name__ == '__main__':
    inner_f = fun('daily_data_prep')
    inner_f()
