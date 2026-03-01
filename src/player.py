from unit import Unit

from inventory import Inventory
from direction import Direction
from item import Item


class Player:
    """
    TODO: ADD DOCSTRING
    """

    marker = Unit.PLAYER

    def __init__(self, x, y):
        """
        TODO: ADD DOCSTRING
        """
        self.pos_x = x
        self.pos_y = y
        self.inventory = Inventory()
        self.is_jumping = False

    def __str__(self):
        """
        TODO: ADD DOCSTRING
        """
        return self.marker.value

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, direction: Direction):
        """Move player in direction.\n
        dx = horisontal movement, relative to player (neg. west, pos. east)\n
        dy = vercial movement, relative to player (neg. north, pos. south)"""
        dx, dy = direction.value
        self.pos_x += dx
        self.pos_y += dy
        self.is_jumping = False

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

    def get_inventory(self):
        """
        TODO: ADD DOCSTRING
        """
        return self.inventory.get_items()

    def add_to_inventory(self, item: Item):
        """
        TODO: ADD DOCSTRING
        """
        self.inventory.add(item)
        print(f"You found a {item.name}, +{item.points} points.")

    def activate_jump(self):
        """
        TODO: ADD DOCSTRING
        """
        self.is_jumping = True
