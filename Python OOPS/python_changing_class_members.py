class Painting:
    type = 'abstract'
    def __init__(self, name, theme):
        self.name = name
        self.theme = theme

print("Before")
a = Painting('Beauty with brain', 'Girl Portrait')
b = Painting('Bhojpur temple', 'Architectural')

print(a.type,b.type)

# print("After")
# a.type = 'Conceptual'
# print(a.type, b.type)

# Correct way to change the value of class variable
print('Using Class Name')
Painting.type = 'ART'
print(a.type, b.type)
