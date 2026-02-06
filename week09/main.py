#create class / object
from week09.inheritanceEx import Person, Staff, Student, print_info


class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_Info(self):
        print(f"Dog Name: {self.name}, Age: {self.age}")
    def __str__(self):
        return f"Dog Name: {self.name}, Age: {self.age} derived from __str__ method"

        
def main():
    print("Hello from USA !")
    print("I love trump")
    my_dog = dog("Buddy", 3)
    my_dog.show_Info()
    your_dog = dog("Max", 5)
    your_dog.show_Info()
    another_dog = dog("Bella", 2)
    another_dog.show_Info()
    print(my_dog)
    p1 = Person("P001", "Alice", 30)
    s1 = Student("S001", "Bob", 20, "ST123")        
    st1 = Staff("ST001", "Charlie", 40, "SF456")

    # เรียกใช้ฟังก์ชันเดียว แต่ผลลัพธ์เปลี่ยนไปตามชนิดของ Object (Polymorphism)
    print_info(p1)   # จะแสดง Name: Alice, Age: 30
    print_info(s1)   # จะแสดง [Student] Bob, ID: ST123
    print_info(st1)  # จะแสดง [Staff] Charlie, Work ID: SF456
    


if __name__ == "__main__":
    main()
  
#cerate object  

