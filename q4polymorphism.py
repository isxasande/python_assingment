class shape:
    def area(self):
        return 0
class Rectangle(shape):
    def _init_(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(shape):
    def _init_(self, radius):
        self.radius = radius
    def area(self):
        return math .pi * (self.radius ** 2)
rect1 = Rectangle("40","100")
print(rect1.area())
circ1 = Circle(20)
print(circ1.area())