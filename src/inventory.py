from item import Item


class Inventory:
    """
    Class representing the player inventory.
    """

    def __init__(self):
        """
        Initializes the Inventory with no items.
        """
        self.items = []

    def __str__(self):
        """
        Display represenation of the inventory.
        """
        display = ""
        for item in self.items:
            if isinstance(item, Item):
                display += f"{item}"
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
        Add an item to the inventory.\n
        item= The item to add to the inventory.
        """
        self.items.append(item)

    def size(self):
        """
        The size of the inventory.\n
        Return: The size of the inventory
        """
        return len(self.items)

    def get_items(self):
        """
        Get all items in the inventory.\n
        """
        return self.items

    def get(self, index):
        """
        Get the item in the inventory at index.\n
        index= The index of the item.\n
        Return: The item at the index.
        """
        if len(self.items) <= index:
            return None
        return self.items[index]
