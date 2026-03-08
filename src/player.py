"""The player class used in the game."""

from .unit import Unit
from .inventory import Inventory
from .direction import Direction
from .item import Item


class Player:
    """The player class."""

    marker = Unit.PLAYER

    def __init__(self, x, y):
        """Initialize the player at position (x,y). WIth an empty inventory.

        x= The horizontal position.
        y= The vertical position.
        """
        self.pos_x = x
        self.pos_y = y
        self.inventory = Inventory()
        self.is_jumping = False

    def __str__(self):
        """Representaton for the player, used to be displayed on the grid."""
        return f"{self.marker}"

    def move(self, direction: Direction):
        """Move player in direction.

        dx = horisontal movement, relative to player (neg. west, pos. east)
        dy = vercial movement, relative to player (neg. north, pos. south)
        """
        dx, dy = direction.value
        new_x = self.pos_x + dx
        new_y = self.pos_y + dy
        self.pos_x = new_x
        self.pos_y = new_y
        self.is_jumping = False

    def can_move(self, direction: Direction, grid):
        """Check if the player can move in a direction.

        dx = horisontal movement, relative to player (neg. west, pos. east)
        dy = vercial movement, relative to player (neg. north, pos. south)
        """
        dx, dy = direction.value
        new_x = self.pos_x + dx
        new_y = self.pos_y + dy
        unit = grid.get(new_x, new_y)
        if unit == Unit.WALL:
            return False
        return True

    def get_inventory(self):
        """Get the player inventory.

        Return: The items in the players inventory.
        """
        return self.inventory.get_items()

    def add_to_inventory(self, item: Item):
        """Att an item to the players inventory.

        item= The item to add to the player inventory.
        """
        self.inventory.add(item)

    def activate_jump(self):
        """Activate the player special jump ability."""
        if self.is_jumping:
            return
        print("Jump activated")
        self.is_jumping = True
