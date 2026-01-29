import os
import json

DATA_FILE = "data.json"


class DataManager:
    """Handles file persistence (JSON storage)"""

    @staticmethod
    def load_data():
        if not os.path.exists(DATA_FILE):
            return {"users": [], "courses": []}
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    @staticmethod
    def save_data(data):
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
