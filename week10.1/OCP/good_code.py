# open-close principle example good_code.py
# Good example of following Open-Closed Principle (OCP)
# สามารถเพิ่มรูปทรงใหม่ได้โดยไม่ต้องแก้ไขฟังก์ชัน calculate_area โอเวอร์ไรด์เมธอด area ในคลาสใหม่

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
object1 = Triangle(10, 5)
object2 = Rectangle(4, 6)
print("Area of Triangle:", object1.area())
print("Area of Rectangle:", object2.area())