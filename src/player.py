from unit import Unit
from inventory import Inventory
from direction import Direction


class Player:
    marker = Unit.PLAYER

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.inventory = Inventory()

    def __str__(self):
        return self.marker.value

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, direction: Direction):
        """Move player in direction.\n
        dx = horisontal movement, relative to player (neg. west, pos. east)\n
        dy = vercial movement, relative to player (neg. north, pos. south)"""
        dx, dy = direction.value
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, direction: Direction, grid):
        """Check if the player can move in a direction.\n
        dx = horisontal movement, relative to player (neg. west, pos. east)\n
        dy = vercial movement, relative to player (neg. north, pos. south)"""
        dx, dy = direction.value
        x = self.pos_x + dx
        y = self.pos_y + dy
        unit = grid.get(x, y)
        if unit == Unit.WALL:
            return False
        return True
