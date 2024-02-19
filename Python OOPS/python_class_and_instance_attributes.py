# Class Attribute - belong to class itself they will be shared by all the instances
# Instance Attribute - not shared by objects

class Painting:
    art1 = 'Painting 1'    # This is a class attribute, it belongs to the class itself and shared by all instances of
    def __init__(self, title):
        self.title = title  # instance attribute
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if len(value) > 50:
            raise ValueError("Title is too long")
        else:
            self._title = value
            
p1 = Painting("Starry Night")
print(p1.title, p1.art1)
p2 = Painting("Mona Lisa")
print(p2.title, p1.art1)

p1.title = "The Weeping Woman"
print(p1.title, p1.art1)
print(p2.title, p2.art1)

# Using class name
Painting.title = "A Scream"  # shared attribute for all instances of Painting   
print(Painting.title)
print(p1.title,p1.art1)
print(p2.title, p2.art1)