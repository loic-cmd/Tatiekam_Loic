
class Course:
    def __init__(self, code, title, capacity):
        self.code = code
        self.title = title
        self.capacity = capacity
        self._students = []  # Enscapsulation

    def add_student(self, student_name):
        if len(self._students) < self.capacity:
            self._students.append(student_name)
            return True
        return False

    def to_dict(self):
        return {
            "code": self.code,
            "title": self.title,
            "capacity": self.capacity,
            "students": self._students,
        }

