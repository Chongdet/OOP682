#isp - interface specification problem
#กล่าวว่า class ควรจะไม่ถูกบังคับให้ implement methods ที่มันไม่ได้ใช้
# bad code example of violating Interface Segregation Principle (ISP) แปลว่า
# class Printer ต้อง implement method print_color แม้ว่าจะไม่ใช้ก็ตาม

class Printer:
    def print_black_and_white(self, document):
        pass
    def print_color(self, document):
        pass 
    
    def scan(self, document):
        pass
        
class SimplePrinter:
    def print_black_and_white(self, document):
        print("Printing in black and white:", document)
    
    def print_color(self, document):
        raise NotImplementedError("This printer does not support color printing.")
    
    def scan(self, document):
        raise NotImplementedError("This printer does not support scanning.")    