from models.classroom import Classroom

my_class = Classroom("101", 30)
my_class.add_student("Alice")
my_class.add_student("Bob")
print(len(my_class))
print(my_class[0])
print(my_class)