"""Module for representing an unit on the game grid."""

from enum import Enum


class Unit(Enum):
    """Unit for the grid."""

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
        """Representation for the unit on the grid."""
        return self.value
