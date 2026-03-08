"""Game state of the game."""

from enum import Enum


class GameState(Enum):
    """Represent the different game states of the game."""

    ACTIVE = "ACTIVE"
    QUIT = "QUIT"
    LOSS = "LOSS"
