''' 
Static Variable 
- allocate memory when the ocject created for the first time
- created outside methos but inside a class
- can be accesde through a class but not directly with an instance
- behaviour is same for every object
'''

class Abstract_Painting:
    type = 'Abstract'
    def __init__(self, name, size):
        self.name = name
        self.size = size

a = Abstract_Painting('Beauty with brain', 'A3')
b = Abstract_Painting('Girls Stare', 'A4')

print(a.type, a.name, a.size)
print(b.type, b.name, b.size)

