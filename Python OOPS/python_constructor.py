# Constructor - used for instantiating an object.
# default constructor
# parameterized constructor

# Destructor - are called when an object gets destroyed. - python has GC that handles memory management automatically.

class Example:
    # #default constructor
    # def __init__(self):
    #     self.name = 'Rita'

    ## parameterized constructor

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Destructor called, Object is being deleted.")

    def print_name(self):
        print(self.name)

o = Example('Rita')
o.print_name()
del o
# o.print_name() # NameError: name 'o' is not defined: Object Deleted