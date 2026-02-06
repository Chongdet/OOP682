from models.person import Person
from models.student import Student
from models.staff import Staff

def print_info(person_obj):
    print(isinstance(person_obj, Person))
    print(person_obj.info())
    
def main():
    p1 = Person("P001", "Alice", 30)
    s1 = Student("S001", "Bob", 20, "ST123")        
    st1 = Staff("ST001", "Charlie", 40, "SF456")

    print_info(p1)   
    print_info(s1)   
    print_info(st1)  
if __name__ == "__main__":
    main()