from unit import Unit


class Item:
    """
    TODO: ADD DOCSTRING
    """

    points = 20

    def __init__(self, name, unit=Unit.ITEM):
        """
        TODO: ADD DOCSTRING
        """
        self.name = name
        self.unit = unit
        self.value = unit.value

    def __str__(self):
        """
        TODO: ADD DOCSTRING
        """
        return self.name
