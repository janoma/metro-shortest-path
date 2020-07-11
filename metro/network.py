import json
from collections import defaultdict
from .station import Station

def readNetworkFromFile(filename: str) -> dict:
    with open(filename) as jsonFile:
        return json.load(jsonFile)

def linesToStationsGraph(lines: dict) -> dict:
    """Converts a collection of lines to a graph of stations."""

    stations = dict()
    for name in lines.keys():
        line = lines[name]
        total = len(line)
        for i in range(total):
            s = line[i]
            stationObj = Station(s.get("id"), s.get("color", None))
            if stationObj not in stations:
                stations[stationObj] = set()
            if i > 0:
                # link with previous station
                stations[stationObj].add(Station(
                    line[i - 1].get("id"), line[i - 1].get("color", None)))
            if i < total - 1:
                # link with next station
                stations[stationObj].add(Station(
                    line[i + 1].get("id"), line[i + 1].get("color", None)))

    return stations

class Network:
    """Represents a metro network."""
    id = 42

    def __init__(self, filename: str):
        """Constructs a metro network from a JSON file."""

        lines = readNetworkFromFile(filename)
