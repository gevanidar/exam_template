from unit import Unit


class Explosion:
    """
    Explosion for visuals after bomb explodes
    """

    explosions = [
        Unit.NORTH_WEST,
        Unit.WEST,
        Unit.SOUTH_WEST,
        Unit.NORTH,
        Unit.MIDDLE,
        Unit.SOUTH,
        Unit.NORTH_EAST,
        Unit.EAST,
        Unit.SOUTH_EAST,
    ]

    def __init__(self, x, y, index=4, time=1):
        """
        Place a explosion tile
        time = time until the explosion fades
        x = horizontal position on grid
        y = vertical position on grid
        index = the index of explosion
        """
        self.time = time
        self.x = x
        self.y = y
        self.value = self.explosions[index]

    def tic(self):
        """
        Reduce the tim for the explosion effect
        """
        self.time -= 1

    def fading(self):
        """
        Check if the explosion faded
        Return: True if the time is left of the explosion is 0
        """
        return self.time == 0
