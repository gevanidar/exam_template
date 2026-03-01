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
    INVENTORY = "i"
    QUIT = "q"
    EXIT = "x"

    def __str__(self):
        return self.value.upper()


class State(Enum):
    RUNNING = "running"
    QUIT = "QUIT"


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
        self.state = State.RUNNING

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
            item = maybe_item
            self.player.add_to_inventory(item)
            self.score += item.points
            self.grid.clear(self.player.pos_x, self.player.pos_y)
        return None

    # TODO: flytta denna till en annan fil
    def print_status(self):
        """Visa spelvärlden och antal poäng."""
        print("--------------------------------------")
        print(f"You have {self.score} points.")
        print(self.grid)

    def start(self):
        while State.RUNNING == self.state:
            game.print_status()

            commands = input(
                f"Use {Input.NORTH}{Input.EAST}{Input.SOUTH}{Input.WEST} to move, {Input.QUIT}/{Input.EXIT} to quit. "
            )
            commands = commands.casefold()
            for i in range(len(commands)):
                command = commands[i]

                match command:
                    case Input.NORTH.value:
                        game.move_player(Direction.NORTH)
                    case Input.EAST.value:
                        game.move_player(Direction.EAST)
                    case Input.SOUTH.value:
                        game.move_player(Direction.SOUTH)
                    case Input.WEST.value:
                        game.move_player(Direction.WEST)
                    case Input.INVENTORY.value:
                        inventory = game.player.get_inventory()
                        if len(inventory) == 0:
                            print("You have no items.")
                        else:
                            inventory_list = "Your inventory consists of:"
                            inventory_list += "".join(
                                [f"\n{item}" for item in inventory]
                            )
                            print(f"{inventory_list}")
                    case Input.EXIT.value:
                        self.state = State.QUIT
                        break
                    case Input.QUIT.value:
                        self.state = State.QUIT
                        break


game = Game()

game.start()

print("Thank you for playing!")
