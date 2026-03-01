from unit import Unit

from inventory import Inventory
from direction import Direction
from item import Item


class Player:
    """
    The player class
    """

    marker = Unit.PLAYER

    def __init__(self, x, y):
        """
        Initialize the player at position (x,y). WIth an empty inventory.\n
        x= The horizontal position.\n
        y= The vertical position.\n
        """
        self.pos_x = x
        self.pos_y = y
        self.inventory = Inventory()
        self.is_jumping = False

    def __str__(self):
        """
        The representaton for the player, used to be displayed on the grid.
        """
        return f"{self.marker}"

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
        Get the player inventory.\n
        Return: The items in the players inventory.
        """
        return self.inventory.get_items()

    def add_to_inventory(self, item: Item):
        """
        Att an item to the players inventory.\n
        item= The item to add to the player inventory.
        """
        self.inventory.add(item)
        print(f"You found a {item.name}, +{item.points} points.")

    def activate_jump(self):
        """
        Activate the player special jump ability.
        """
        self.is_jumping = True
