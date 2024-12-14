# Divi Newton
# November 17, 2023
# Quiz 4
# collaborators: Dylan Ravel

import math
class Shapes():
    def __init__(self, sides, length):
        self.sides = sides
        self.length = length

    def area(self):
        if self.sides == 3:
            return ((math.sqrt(3) / 4) * (self.length ** 2))
        elif self.sides == 4:
            return (self.length * self.sides)
        elif self.sides == 6:
            return ((3 * (math.sqrt(3)) * (self.length ** 2)) / 2)
        
    def perimeter(self):
        return self.sides * self.length
    

triangle1 = Shapes(3, 10)
square1 = Shapes(4, 10)
hexagon1 = Shapes(6, 10)

print("Triangle:")
print(triangle1.area())
print(triangle1.perimeter())

print("Square:")
print(square1.area())
print(square1.perimeter())

print("Hexagon:")
print(hexagon1.area())
print(hexagon1.perimeter())