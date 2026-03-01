from enum import Enum
import random
from math import floor

from grid import Grid
from player import Player
from pickups import randomize
from item import Item
from direction import Direction


class Input(Enum):
    NORTH = "w"
    EAST = "d"
    SOUTH = "s"
    WEST = "a"


class Game:
    def __init__(self):
        """Initialize the game."""
        g = Grid()
        width, height = g.size()
        assert width > 10
        assert height > 10
        dx = 2
        dy = 2
        mid_x = floor(width / 2)
        mid_y = floor(height / 2)
        x = random.randint(mid_x - dx, mid_x + dx)
        y = random.randint(mid_y - dy, mid_y + dy)
        player = Player(x, y)
        g.set_player(player)
        g.make_walls()
        randomize(g)

        self.grid = g
        self.player = player
        self.score = 0

    def move_player(self, direction: Direction):
        """Move the player on the grid in the direction\n
        direction = the direction to move the player"""
        dir = direction.value
        new_pos = (self.player.pos_x + dir[0], self.player.pos_y + dir[1])
        if not self.player.can_move(direction, self.grid):
            unit = self.grid.get(new_pos[0], new_pos[1])
            print(f"I cannot move {direction} because a {unit.value} is in the way.")
            return
        maybe_item = self.grid.get(new_pos[0], new_pos[1])

        self.player.move(direction)

        if isinstance(maybe_item, Item):
            # we found something
            self.score += maybe_item.points
            print(f"You found a {maybe_item.name}, +{maybe_item.points} points.")
            # g.set(player.pos_x, player.pos_y, Unit.EMPTY)
            self.grid.clear(self.player.pos_x, self.player.pos_y)
        return None

    # TODO: flytta denna till en annan fil
    def print_status(self):
        """Visa spelvärlden och antal poäng."""
        print("--------------------------------------")
        print(f"You have {self.score} points.")
        print(self.grid)


game = Game()


command = "a"
# Loopa tills användaren trycker Q eller X.
while command.casefold() not in ["q", "x"]:
    game.print_status()

    commands = input("Use WASD to move, Q/X to quit. ")
    commands = commands.casefold()
    print(Input.NORTH.value)
    for i in range(len(commands)):
        command = commands[i]

        print(f"Processing command {command}")
        match command:
            case Input.NORTH.value:
                game.move_player(Direction.NORTH)
            case Input.EAST.value:
                game.move_player(Direction.EAST)
            case Input.SOUTH.value:
                game.move_player(Direction.SOUTH)
            case Input.WEST.value:
                game.move_player(Direction.WEST)
            case "i":
                print(game.player.inventory)


# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")
