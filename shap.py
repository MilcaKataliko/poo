from abc import ABC

class Shape(ABC):
    def area(self):
        return 0


class Sqare(Shape):
    def __init__(self, lenghth):
        self.lenghth = lenghth
    def area(self):
        return self.lenghth * self.lenghth
Sqare = Sqare(4)
square_area = Sqare.area()
print(square_area)

class Triangle(Shape):
    def __init__(self, hauteur, base):
        self.base = base
        self.hauteur = hauteur
        self.base = base
    def area(self):
        return (self.hauteur * self.base)/2
triangle = Triangle(7,5)    
surface = triangle.area()
print(surface) 

                  