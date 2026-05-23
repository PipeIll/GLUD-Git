import json


def read_json(path):
    try:
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []