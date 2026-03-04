"""Helped module for generating pickups on game grid."""

import random
from .item import Item
from .grid import Grid

pickups = [
    Item("carrot"),
    Item("apple"),
    Item("strawberry"),
    Item("cherry"),
    Item("watermelon"),
    Item("radish"),
    Item("cucumber"),
    Item("meatball"),
]


def randomize(grid: Grid):
    """Randomize all pickups on the grid.

    grid= The grid to populate with the pickups.
    """
    for item in pickups:
        add_pickup(grid, item)


def add_random_pickup(grid: Grid):
    """Add a random pickup item to the grid.

    grid= The grid to populate with the pickup.
    """
    add_pickup(grid, pickups[random.randint(0, len(pickups) - 1)])


def add_pickup(grid: Grid, item: Item):
    """Add an item to the grid.

    grid= The grid to populate with the item.
    """
    x, y = grid.randomized_empty_position(0, 0, grid.width - 1, grid.height - 1)
    grid.set(x, y, item)
