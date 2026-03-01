from enum import Enum


class GameState(Enum):
    """
    Game state for if the game is currently active, if the player stopped the game or if the player lost.
    """

    ACTIVE = "ACTIVE"
    QUIT = "QUIT"
    LOSS = "LOSS"
