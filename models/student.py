from models.user import User

class Student(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.registered_courses = []

    def get_role(self):  # Polymorphism
        return "Student"

    def register_course(self, course):
        if course.add_student(self.username):
            self.registered_courses.append(course.code)
            print("Course registered successfully.")
        else:
            print("Course is full")
