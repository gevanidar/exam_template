from unit import Unit


class Item:
    """
    Representing an Item
    """

    points = 20

    def __init__(self, name, unit=Unit.ITEM):
        """
        Initialize the item with a name and as a Unit.\n
        name= The name of the item.\n
        unit= The unit type of the item. Default is Unit.ITEM.
        """
        self.name = name
        self.unit = unit
        self.value = unit.value

    def __str__(self):
        """
        The string representation of the item.
        Return: The name of the item
        """
        return self.unit
