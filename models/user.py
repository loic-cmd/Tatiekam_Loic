
class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password  # Enscapsulation

    def authenticate(self, password):
        return self._password == password

    def get_role(self):
        raise NotImplementedError("Subclasses must implement this method")

