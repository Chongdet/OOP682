# good idea example good_code.py
# Good example of following Interface Segregation Principle (ISP)
# แยก interface ออกเป็นส่วนย่อยๆ เพื่อให้ class ต่างๆ implement เฉพาะ methods ที่จำเป็นต้องใช้

from abc import ABC, abstractmethod
class PrinterInterface(ABC):
    @abstractmethod
    def print_black_and_white(self, document):
        pass
    @abstractmethod
    def print_color(self, document):
        pass
    
class ScannerInterface(ABC):
    @abstractmethod
    def scan(self, document):
        pass
    
class SimplePrinter(PrinterInterface):
    def print_black_and_white(self, document):
        print("Printing in black and white:", document)
    
    def print_color(self, document):
        raise NotImplementedError("This printer does not support color printing.")
    
class AdvancedPrinter(PrinterInterface, ScannerInterface):
    def print_black_and_white(self, document):
        print("Printing in black and white:", document)
    
    def print_color(self, document):
        print("Printing in color:", document)
    
    def scan(self, document):
        print("Scanning document:", document)
        
# Example usage
simple_printer = SimplePrinter()
simple_printer.print_black_and_white("Test Document")
advanced_printer = AdvancedPrinter()
advanced_printer.print_color("Color Document")
advanced_printer.scan("Scanned Document")