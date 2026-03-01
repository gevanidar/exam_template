from enum import Enum


class Input(Enum):
    """
    Allowed input keys
    """

    MOVE_NORTH = "w"
    MOVE_EAST = "d"
    MOVE_SOUTH = "s"
    MOVE_WEST = "a"
    SHOW_INVENTORY = "i"
    QUIT_GAME = "q"
    EXIT_GAME = "x"
    ACTIVATE_JUMP = "j"
    PLACE_BOMB = "b"
    DISARM_TRAP = "t"
    SHOW_HELP = "h"

    def __str__(self):
        return self.value.upper()

    def description(self):
        return f"{self.name.lower().replace('_', ' ')}"

    def explanation(self):
        return f"Press key {self} to {self.description()}"
