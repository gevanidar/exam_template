from enum import Enum


class Unit(Enum):
    EMPTY = "."
    WALL = "■"
    ITEM = "?"
    PLAYER = "@"
    TRAP = "!"
    NORTH_WEST = "\\"
    WEST = "-"
    SOUTH_WEST = "/"
    NORTH = "|"
    MIDDLE = "*"
    SOUTH = "|"
    NORTH_EAST = "/"
    EAST = "-"
    SOUTH_EAST = "\\"

    def __str__(self):
        return self.value
