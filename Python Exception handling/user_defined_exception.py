class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return(repr(self.value))


try:
    raise(MyError(10))
except MyError as error:
    print(f"Caught an exception with values {error.value}")