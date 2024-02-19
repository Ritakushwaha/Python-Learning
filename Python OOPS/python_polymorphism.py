# def add(x,y,z=0):
#     return x+y+z

# print(add(2,3))
# print(add(10,9,8))


class Paintings:
    def name(self):
        print("Beauty with brain")
    def type(self):
        print("Abstract")
    def size(self):
        print('A3')

class Water_Color():
    def name(self):
        print("Bhojpur Temple Painting")
    def type(self):
        print('Realistic')
    def size(self):
        print('A4')

obj = Paintings()
obj_water_color = Water_Color()

for _ in (obj, obj_water_color):
    _.name()
    _.type()
    _.size()