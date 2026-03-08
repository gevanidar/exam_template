"""Enum representation of the allowed inputs for the game."""

from enum import Enum


class Input(Enum):
    """Allowed input keys."""

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
        """Representation for the key."""
        return self.value.upper()

    def description(self):
        """Display a human readable description of what the input does."""
        return f"{self.name.lower().replace('_', ' ')}"

    def explanation(self):
        """Show an explanation of key to press and what happens whn pressed."""
        return f"Press key {self} to {self.description()}"
