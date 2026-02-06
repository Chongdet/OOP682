class Classroom:
    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity
        self.students = []
        
    def add_student(self, student):
            self.students.append(student)

    def __str__(self):
        return f"Classroom[Room Number: {self.room_number}, Capacity: {self.capacity}]"
    
    def __len__(self):
        return self.capacity
    
    def __getitem__(self, index):
        return self.students[index]