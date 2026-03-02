class Bomb:
    """
    Bomb class for representing a time dependent explosive
    """

    def __init__(self, x, y, time=3):
        """
        Places the bomb and starts the fuse
        time = time until the bomb explodes
        x = horizontal position on grid
        y = vertical position on grid
        """
        self.time = time
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.time}"

    def tic(self):
        """
        Reduces the time until bomb explodes.
        """
        self.time -= 1
        print(
            f"Bomb fuse is burning, move away from the ({self.x},{self.y}) area ({self.time} moves left)"
        )

    def is_exploding(self):
        """
        Checks if the bomb explodes
        Return: True if there is no more time left
        """
        return self.time == 0
