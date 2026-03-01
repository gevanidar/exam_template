from unit import Unit


class Trap:
    """
    Representing a Trap
    """

    points = -10

    def __init__(self, unit=Unit.TRAP):
        """
        Initialize the item with a name and as a Unit.\n
        name= The name of the item.\n
        unit= The unit type of the item. Default is Unit.ITEM.
        """
        self.unit = unit
        self.value = unit.value
