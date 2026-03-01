from enum import Enum

from grid import Grid
from player import Player
from pickups import randomize
from item import Item


class Input(Enum):
    NORTH = "w"
    EAST = "d"
    SOUTH = "s"
    WEST = "a"


class Direction(Enum):
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)

    def __str__(self):
        return self.name.lower()


class Game:
    def __init__(self):
        player = Player(2, 1)

        g = Grid()
        g.set_player(player)
        g.make_walls()
        randomize(g)
        self.grid = g
        self.player = player
        self.score = 0

    def move(self, direction: Direction):
        dir = direction.value
        new_pos = (self.player.pos_x + dir[0], self.player.pos_y + dir[1])
        if not self.player.can_move(dir[0], dir[1], self.grid):
            unit = self.grid.get(new_pos[0], new_pos[1])
            print(f"I cannot move {direction} because a {unit.value} is in the way.")
            return
        maybe_item = self.grid.get(new_pos[0], new_pos[1])

        self.player.move(dir[0], dir[1])

        if isinstance(maybe_item, Item):
            # we found something
            self.score += maybe_item.points
            print(f"You found a {maybe_item.name}, +{maybe_item.points} points.")
            # g.set(player.pos_x, player.pos_y, Unit.EMPTY)
            self.grid.clear(self.player.pos_x, self.player.pos_y)
        return None


game = Game()


# TODO: flytta denna till en annan fil
def print_status(game: Game):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {game.score} points.")
    print(game.grid)


command = "a"
# Loopa tills användaren trycker Q eller X.
while command.casefold() not in ["q", "x"]:
    print_status(game)

    commands = input("Use WASD to move, Q/X to quit. ")
    commands = commands.casefold()
    print(Input.NORTH.value)
    for i in range(len(commands)):
        command = commands[i]

        print(f"Processing command {command}")
        match command:
            case Input.NORTH.value:
                game.move(Direction.NORTH)
            case Input.EAST.value:
                game.move(Direction.EAST)
            case Input.SOUTH.value:
                game.move(Direction.SOUTH)
            case Input.WEST.value:
                game.move(Direction.WEST)
            case "i":
                print(game.player.inventory)


# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")
