from models.person import Person


class Student(Person):
    def __init__(self, pid, name, age, student_id):
        super().__init__(pid, name, age)
        self.student_id = student_id

    def info(self):  # Overriding
        return f"[Student] {self.name}, ID: {self.student_id}"
