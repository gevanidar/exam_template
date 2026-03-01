import random
from item import Item
from grid import Grid

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
    """
    Randomize all pickups on the grid.\n
    grid= The grid to populate with the pickups.
    """
    for item in pickups:
        add_pickup(grid, item)


def add_random_pickup(grid: Grid):
    """
    Adds a random pickup item to the grid.\n
    grid= The grid to populate with the pickup.
    """
    add_pickup(grid, pickups[random.randint(0, len(pickups) - 1)])


def add_pickup(grid: Grid, item: Item):
    """
    Adds an item to the grid.\n
    grid= The grid to populate with the item.
    """
    while True:
        x = grid.get_random_x()
        y = grid.get_random_y()
        if grid.is_empty(x, y):
            grid.set(x, y, item)
            break
