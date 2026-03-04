"""Game state for if the game is currently active,
if the player stopped the game or if the player lost."""

from enum import Enum


class GameState(Enum):
    """Represent the different game states of the game."""

    ACTIVE = "ACTIVE"
    QUIT = "QUIT"
    LOSS = "LOSS"
