class Bomb:
    """
    TODO: ADD DOCSTRING
    """

    def __init__(self, x, y, time=3):
        """
        TODO: ADD DOCSTRING
        """
        self.time = time
        self.x = x
        self.y = y

    def tic(self):
        """
        TODO: ADD DOCSTRING
        """
        print(
            f"Bomb fuse is burning, move away from the ({self.x},{self.y}) area ({self.time} moves left)"
        )
        self.time -= 1

    def is_exploding(self):
        """
        TODO: ADD DOCSTRING
        """
        return self.time == 0
