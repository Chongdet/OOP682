# LSP good_idea.py
# Good example of following Liskov Substitution Principle (LSP)
# subclass Square สามารถแทนที่ superclass Rectangle ได้อย่างสมบูรณ์
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape): #สี่เหลี่ยมผืนผ้า
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height
    
class Square(Shape): #สี่เหลี่ยมจัตุรัส
    def __init__(self, side):
        self.side = side

    def set_side(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
    
def resize_shape(shape, new_size):
    if isinstance(shape, Rectangle):
        shape.set_width(new_size)
        shape.set_height(new_size)
    elif isinstance(shape, Square):
        shape.set_side(new_size)
    return shape.area()

# Example usage
rect = Rectangle(4, 5)
square = Square(4)
print("Area of Rectangle:", resize_shape(rect, 6))  # Output: Area of Rectangle: 36
print("Area of Square:", resize_shape(square, 6))    # Output: Area of