from enum import Enum


class Direction(Enum):
    """
    TODO: ADD DOCSTRING
    """

    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)

    def __str__(self):
        return self.name.lower()
