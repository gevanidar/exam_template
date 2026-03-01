from enum import Enum


class Input(Enum):
    """
    Allowed input keys
    """

    NORTH = "w"
    EAST = "d"
    SOUTH = "s"
    WEST = "a"
    INVENTORY = "i"
    QUIT = "q"
    EXIT = "x"
    JUMP = "j"
    BOMB = "b"
    TRAP = "t"

    def __str__(self):
        return self.value.upper()
