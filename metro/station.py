from enum import Enum
from termcolor import colored

class Color(Enum):
    red = 1
    green = 2

def colorFromStr(val: str) -> Color:
    if val == "red":
        return Color.red
    if val == "green":
        return Color.green
    return None

class Station:
    name: str
    color: Color = None

    def __init__(self, name: str, color: str = None):
        self.name = name
        self.color = colorFromStr(color)

    def __eq__(self, other):
        # Why this is not the default behavior is beyond me,
        # but certainly something to investigate (new to python classes).
        if not isinstance(other, Station):
            return NotImplemented

        return self.name == other.name and self.color == other.color

    def __hash__(self):
        # Why this is not the default behavior is beyond me,
        # but certainly something to investigate (new to python classes).
        return hash((self.name, self.color))

    def __repr__(self):
        if self.color == Color.red:
            return colored(self.name, "red")
        if self.color == Color.green:
            return colored(self.name, "green")
        return self.name
