import json
from collections import defaultdict

def read_network_from_file(filename: str) -> dict:
    with open(filename) as jsonFile:
        return json.load(jsonFile)
