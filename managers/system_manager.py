from managers.data_manager import DataManager
from models.student import Student
from models.admin import Admin
from models.course import Course

class SystemManager:
    def __init__(self):
        self.data = DataManager.load_data()
        self.users = self.data["users"]
        self.courses = self.data["courses"]

    def save(self):
        DataManager.save_data(self.data)

    def register_user(self, role):
        username = input("Username: ")
        password = input("Password: ")

        self.users.append({"username": username, "password": password, "role": role})
        self.save()
        print("User registered successfully")

    def login(self):
        username = input("Username: ")
        password = input("Password: ")

        for user in self.users:
            if user["username"] == username and user["password"] == password:
                if user["role"] == "student":
                    return Student(username, password)
                else:
                    return Admin(username, password)
        print("Invalid login.")
        return None

    def add_course(self):
        code = input("Course code: ")
        title = input("Course Title: ")
        capacity = int(input("Capacity: "))

        course = Course(code, title, capacity)
        self.courses.append(course.to_dict())
        self.save()
        print("Course added successfully")

    def list_courses(self):
        for course in self.courses:
            print(
                f"{course['code']} - {course['title']} "
                f"({len(course['students'])}/{course['capacity']})"
            )

    def run(self):
        while True:
            print("\n Main Menu \n")
            print("1. Register as Student")
            print("2. Register as Admin")
            print("3. Login")
            print("4. Exit program")

            choice = input("Select option: ")

            if choice == "1":
                self.register_user("student")

            elif choice == "2":
                self.register_user("admin")

            elif choice == "3":
                user = self.login()
                if not user:
                    continue

                if user.get_role() == "Student":
                    while True:
                        print("\n Student Menu")
                        print("1. View courses")
                        print("2. Logout")

                        student_choice = input("Select an Option: ")
                        if student_choice == "1":
                            self.list_courses()
                        elif student_choice == "2":
                            break
                        else:
                            print("Invalid Option")
                elif user.get_role() == "Admin":
                    while True:
                        print("\n Admin Menu")
                        print("1. Add Course")
                        print("2. View Courses")
                        print("3. Logout")

                        admin_choice = input("Choose: ")

                        if admin_choice == "1":
                            self.add_course()
                        elif admin_choice == "2":
                            self.list_courses()
                        elif admin_choice == "3":
                            break
                        else:
                            print("Invalid Option")
            elif choice == "4":
                print("Exiting program...")
                break

            else:
                print("Invalid Option")
