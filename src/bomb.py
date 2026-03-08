"""Module for representing a bomb in the game."""


class Bomb:
    """Bomb class for representing a time dependent explosive."""

    def __init__(self, x, y, time=3):
        """Places the bomb and starts the fuse.

        time = time until the bomb explodes.
        x = horizontal position on grid.
        y = vertical position on grid.
        """
        self.time = time
        self.x = x
        self.y = y

    def __str__(self):
        """Representation of the bomb."""
        return f"{self.time}"

    def tic(self):
        """Reduces the time until bomb explodes."""
        self.time -= 1

    def is_exploding(self):
        """Check if the bomb explodes.

        Return: True if there is no more time left.
        """
        return self.time == 0
