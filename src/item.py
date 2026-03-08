"""Module for representing an item in the game."""

from .unit import Unit


class Item:
    """Representing an Item."""

    points = 20

    def __init__(self, name, unit=Unit.ITEM):
        """Initialize the item with a name and as a Unit.

        name= The name of the item.
        unit= The unit type of the item. Default is Unit.ITEM.
        """
        self.name = name
        self.unit = unit
        self.value = unit.value

    def get_points(self):
        """Get the number of points gained when picking up an item.

        Returns: the number of points from picking up an item.
        """
        return self.points
