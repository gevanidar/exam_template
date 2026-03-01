import random
from unit import Unit


class Grid:
    """Representerar spelplanen. Du kan ändra standardstorleken och tecknen för olika rutor."""

    width = 20
    height = 12

    def __init__(self):
        """Skapa ett objekt av klassen Grid"""
        # Spelplanen lagras i en lista av listor. Vi använder "list comprehension" för att sätta tecknet för "empty" på varje plats på spelplanen.
        self.data = [
            [Unit.EMPTY for y in range(self.width)] for z in range(self.height)
        ]

    def size(self):
        return self.width, self.height

    def get(self, x, y):
        """Hämta det som finns på en viss position"""
        return self.data[y][x]

    def set(self, x, y, value):
        """Ändra vad som finns på en viss position"""
        self.data[y][x] = value

    def set_player(self, player):
        self.player = player

    def clear(self, x, y):
        """Ta bort item från position"""
        self.set(x, y, Unit.EMPTY)

    def boundary_check(self, x, y):
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    def __str__(self):
        """Gör så att vi kan skriva ut spelplanen med print(grid)"""
        xs = ""
        for y in range(len(self.data)):
            row = self.data[y]
            for x in range(len(row)):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += f"{self.player}"
                else:
                    xs += str(row[x].value)
            xs += "\n"
        return xs

    def make_walls(self):
        """Skapa väggar runt hela spelplanen"""
        self.make_room(0, 0, self.width - 1, self.height - 1)

        assert self.width >= 20
        assert self.height >= 12

        # Hardcoded -> Could be implemented using some smart algorithm
        self.make_room(0, 0, 5, 5)
        self.make_room(self.width - 8, 2, self.width - 3, 6)
        self.make_room(4, self.height - 5, self.width - 3, self.height - 2)
        self.make_room(7, self.height - 5, self.width - 3, self.height - 2)

        self.clear(3, 5)
        self.clear(self.width - 8, 4)
        self.clear(self.width - 6, 6)
        self.clear(self.width - 6, 7)
        self.clear(4, self.height - 4)
        self.clear(8, self.height - 2)
        self.clear(8, self.height - 1)

    def make_room(self, start_x, start_y, stop_x, stop_y):
        """Create a room starting at start_x, start_y"""
        for y in range(start_y, stop_y):
            if self.is_empty(start_x, y):
                self.set(start_x, y, Unit.WALL)
            if self.is_empty(stop_x, y):
                self.set(stop_x, y, Unit.WALL)

        for x in range(start_x, stop_x):
            if self.is_empty(x, start_y):
                self.set(x, start_y, Unit.WALL)
            if self.is_empty(x, stop_y):
                self.set(x, stop_y, Unit.WALL)

        if self.is_empty(stop_x, stop_y):
            self.set(stop_x, stop_y, Unit.WALL)

    # Används i filen pickups.py
    def get_random_x(self):
        """Slumpa en x-position på spelplanen"""
        return random.randint(0, self.width - 1)

    def get_random_y(self):
        """Slumpa en y-position på spelplanen"""
        return random.randint(0, self.height - 1)

    def is_empty(self, x, y):
        """Returnerar True om det inte finns något på aktuell ruta"""
        return self.get(x, y) == Unit.EMPTY

    def is_obstacle(self, x, y):
        """Returnerar True if the position contains and obstacle"""
        return self.get(x, y) == Unit.WALL
