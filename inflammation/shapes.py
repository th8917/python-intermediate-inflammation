import math

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def get_area(self):
        return math.pi *self.radius*self.radius

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height 

    def get_area(self):
        return self.width*self.height
        
    

my_circle = Circle(15)
print(my_circle.get_area())
another_circle = Circle(15)
my_rect = Rectangle(10,20)

my_shapes =[my_circle,my_rect]

for shapes in my_shapes:
    print(shapes.get_area())