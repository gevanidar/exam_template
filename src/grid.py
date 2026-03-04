"""Module used for representing the grid and rules on the grid."""

import random

from .unit import Unit
from .trap import Trap
from .bomb import Bomb


class Grid:
    """Representation of the grid for the game."""

    width = 20
    height = 12

    def __init__(self):
        """Create an empty grid."""
        self.data = [
            [Unit.EMPTY for y in range(self.width)] for z in range(self.height)
        ]
        self.bombs = []
        self.player = None

    def randomized_empty_position(self, x_min, y_min, x_max, y_max):
        """Get an empty position (x,y) from the grid.

        x_min= the min x value to select from.
        y_min= the min y value to select from.
        x_max= the max x value to select from.
        y_max= the max y value to select from.
        Return: The position (x,y)
        """
        assert self.boundary_check(x_min, y_min)
        assert self.boundary_check(x_max, y_max)
        x = 0
        y = 0
        while not self.is_empty(x, y):
            x = random.randint(x_min, x_max)
            y = random.randint(y_min, y_max)
        return x, y

    def size(self):
        """Size of the grid.

        Return: A tuple of the (width, height).
        """
        return self.width, self.height

    def get(self, x, y):
        """Get the Unit data from position (x,y)."""
        if not self.boundary_check(x, y):
            return None
        return self.data[y][x]

    def set(self, x, y, value):
        """Set the Unit data on position (x,y)."""
        if not self.boundary_check(x, y):
            return
        self.data[y][x] = value

    def set_player(self, player):
        """Set the player on the grid.

        Player: the player.
        """
        self.player = player

    def put_bomb(self, bomb):
        """Add a bomb to the bombs list.

        Bomb: the bomb.
        """
        self.bombs.append(bomb)

    def tic_bombs(self):
        """Tic all bombs."""
        number_of_bombs = len(self.bombs)
        if number_of_bombs == 0:
            return

        for bomb in self.bombs:
            bomb.tic()

    def explode_bomb(self):
        """Explode the bomb with the lowest time left (first in list)."""
        number_of_bombs = len(self.bombs)
        if number_of_bombs == 0:
            return None

        bomb: Bomb = self.bombs[0]
        if not bomb.is_exploding():
            return None

        self.bombs = self.bombs[1:]
        self.clear(bomb.x, bomb.y)
        print("KABOOM!")
        return bomb

    def set_trap(self, x, y):
        """Set the trap on the grid.

        Trap: the trap.
        """
        trap = Trap()

        self.set(x, y, trap)

    def destroy(self, x, y):
        """Destoy any non-empty unit on the grid at position (x,y).

        x= The horizontal position.
        y= The vertical position.
        """
        if not self.boundary_check(x, y):
            return
        unit = self.get(x, y)
        if Unit.EMPTY == unit:
            return
        print(f"Bomb destroyed {unit} at position ({x},{y})")
        self.clear(x, y)

    def clear(self, x, y):
        """Clear any positon (x,y) on the grid."""
        if not self.boundary_check(x, y):
            return
        self.set(x, y, Unit.EMPTY)

    def boundary_check(self, x, y):
        """Check if the position (x,y) is within the grid boundaries.

        Return: True if both x and y are within the grid boundaries.
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def __str__(self):
        """Display the grid."""
        xs = ""
        for y, row in enumerate(self.data):
            for x, col in enumerate(row):
                if self.player and x == self.player.pos_x and y == self.player.pos_y:
                    xs += f"{self.player}"
                else:
                    value = str(col.value)
                    for bomb in self.bombs:
                        bomb: Bomb = bomb
                        if x == bomb.x and y == bomb.y:
                            value = f"{bomb}"
                            break
                    xs += value
            xs += "\n"
        return xs

    def make_walls(self):
        """Create walls and rooms onthe grid."""
        self.make_room(0, 0, self.width - 1, self.height - 1)

        assert self.width >= 20
        assert self.height >= 12

        # Hardcoded -> Could be implemented using some smart algorithm
        # Walls for the rooms
        self.make_room(0, 0, 5, 5)
        self.make_room(self.width - 8, 2, self.width - 3, 6)
        self.make_room(4, self.height - 5, self.width - 3, self.height - 2)
        self.make_room(7, self.height - 5, self.width - 3, self.height - 2)

        # "Doors" for the rooms
        self.clear(3, 5)
        self.clear(self.width - 8, 4)
        self.clear(self.width - 6, 6)
        self.clear(self.width - 6, 7)
        self.clear(4, self.height - 4)
        self.clear(8, self.height - 2)
        self.clear(8, self.height - 1)

    def make_room(self, start_x, start_y, stop_x, stop_y):
        """Create a room.

        start_x= The left wall  of the room.
        stop_x= The right wall of the room.
        start_y= The upper wall of the room.
        stop_x= The lower wall  of the room.
        """
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
        """Generate a random x value within the grid boundaries."""
        return random.randint(0, self.width - 1)

    def get_random_y(self):
        """Generate a radom y value within the gid boundaries."""
        return random.randint(0, self.height - 1)

    def is_empty(self, x, y):
        """Check if the position (x,y) is empty.

        x= The horizontal position.
        y= The vertical position.
        Return: True if position is empty
        """
        return self.get(x, y) == Unit.EMPTY

    def is_trap(self, x, y):
        """Return true if the position contains a trap.

        x= The horizontal position.
        y= The vertical position.
        Return: True if position contains a Trap.
        """
        return isinstance(self.get(x, y), Trap)

    def is_obstacle(self, x, y):
        """Return true if the position contains and obstacle.

        x= The horizontal position.
        y= The vertical position.
        Return: True if position contains an obstacle
        """
        return self.get(x, y) == Unit.WALL
