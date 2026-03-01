from item import Item


class Inventory:
    def __init__(self):
        self.items = []

    def __str__(self):
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

    def get(self, index):
        if len(self.items) <= index:
            return None
        return self.items[index]
