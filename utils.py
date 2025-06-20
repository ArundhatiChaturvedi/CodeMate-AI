import json

def load_user_data():
    with open("data/user_data.json", "r") as f:
        return json.load(f)

def save_user_data(data):
    with open("data/user_data.json", "w") as f:
        json.dump(data, f, indent=4)
