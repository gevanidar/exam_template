"""Representation of the allowed movement directions in the game."""

from enum import Enum


class Direction(Enum):
    """A Direction allowedon the drid in a readable format."""

    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)

    def __str__(self):
        """Representationof the direction in a human readable form."""
        return self.name.lower()
