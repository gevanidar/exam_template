from item import Item


class Inventory:
    """
    TODO: ADD DOCSTRING
    """

    def __init__(self):
        """
        TODO: ADD DOCSTRING
        """
        self.items = []

    def __str__(self):
        """
        TODO: ADD DOCSTRING
        """
        display = ""
        for item in self.items:
            if isinstance(item, Item):
                display += item.value
                display += ","
            else:
                display += "Non-item found("
                display += item
                display += ")"
                display += ","
        display.rstrip(",")
        return display

    def add(self, item: Item):
        """
        TODO: ADD DOCSTRING
        """
        self.items.append(item)

    def size(self):
        """
        TODO: ADD DOCSTRING
        """
        return len(self.items)

    def get_items(self):
        """
        TODO: ADD DOCSTRING
        """
        return self.items

    def get(self, index):
        """
        TODO: ADD DOCSTRING
        """
        if len(self.items) <= index:
            return None
        return self.items[index]
