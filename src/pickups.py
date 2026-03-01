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
    for item in pickups:
        add_pickup(grid, item)


def add_random_pickup(grid: Grid):
    add_pickup(grid, pickups[random.randint(0, len(pickups) - 1)])


def add_pickup(grid: Grid, item: Item):
    while True:
        x = grid.get_random_x()
        y = grid.get_random_y()
        if grid.is_empty(x, y):
            grid.set(x, y, item)
            break
