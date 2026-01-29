from models.user import User

class Admin(User):
    def get_role(self):  # Polymorphism
        return "Admin"
