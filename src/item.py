from unit import Unit


class Item:
    points = 20

    """Representerar saker man kan plocka upp."""

    def __init__(self, name, unit=Unit.ITEM):
        self.name = name
        self.unit = unit
        self.value = unit.value

    def __str__(self):
        return self.name
