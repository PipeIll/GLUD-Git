import json


def read_json(path):
    try:
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    

def write_json(path, data):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)