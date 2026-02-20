#Liskov Substitution Principle (LSP) violation example bad_idea.py
# Bad example of violating Liskov Substitution Principle (LSP)
# subclass Square ไม่สามารถแทนที่ superclass Rectangle ได้อย่างสมบูรณ์
# เนื่องจากการตั้งค่าความกว้างและความสูงของ Square ส่งผลกระทบต่อกัน
class Rectangle: #สี่เหลี่ยมผืนผ้า
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
        
class Square(Rectangle): #สี่เหลี่ยมจัตุรัส
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, width):
        self.width = width
        self.height = width  
 
    def set_height(self, height):
        self.height = height
        self.width = height 

def resize_rectangle(rectangle, new_width, new_height):
    rectangle.set_width(new_width)
    rectangle.set_height(new_height)
    return rectangle.width * rectangle.height

# Example usage
rect = Rectangle(4, 5)
square = Square(4)
print("Area of Rectangle:", resize_rectangle(rect, 6, 7))  # Output: Area of Rectangle: 42
print("Area of Square:", resize_rectangle(square, 6, 7))    # Output
