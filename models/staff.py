from models.person import Person


class Staff(Person):
    def __init__(self, pid, name, age, staff_id):
        super().__init__(pid, name, age)
        self.staff_id = staff_id

    def info(self):  # Overriding
        return f"[Staff] {self.name}, Work ID: {self.staff_id}"
