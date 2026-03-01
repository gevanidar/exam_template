from enum import Enum


class Unit(Enum):
    EMPTY = "."
    WALL = "■"
    ITEM = "?"
    PLAYER = "@"
    TRAP = "!"

    def __str__(self):
        return self.value
