class Rectangle:
    def __init__(self, width, length,):
        self.width = width
        self.length = length

    def area(self):
        return (self.width * self.length)

    def get_area(self):
        print(f"rectangle area: {self.area()}")

    def perimeter(self):
        print(f"rectangle perimeter: {(2*self.width) + (2*self.length)}")
from math import sqrt, pi
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        print(f"circle area: {round(pi* (self.radius**2))}")

    def perimeter(self):
        print(f"circle circumference: {round(2*self.radius * pi)}")

rectangle1 = Rectangle(5, 4)

rectangle1.get_area()

rectangle1.perimeter()

circle1 = Circle(5)

circle1.area()

circle1.perimeter()