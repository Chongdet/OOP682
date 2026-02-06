class Person:
    def __init__(self, pid, name, age):
        self.pid = pid
        self.name = name
        self.age = age

    def info(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    def __str__(self):
        return f"Person[ID: {self.pid}, Name: {self.name}, Age: {self.age}]"
