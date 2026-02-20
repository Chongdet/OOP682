#open-close principle violation example
# Bad example of violating Open-Closed Principle (OCP)
#ไม่สามรถเพิ่มรูปทรงใหม่ได้โดยไม่แก้ไขฟังก์ชัน calculate_area
class Circle:
    def __init__(self, radius):
        self.radius = radius

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

def calculate_area(shape):
    if isinstance(shape, Circle):
        return 3.14 * shape.radius * shape.radius
    elif isinstance(shape, Rectangle):
        return shape.width * shape.height
    elif isinstance(shape, Triangle):
        return 0.5 * shape.base * shape.height
    else:
        raise TypeError("Unknown shape type")