from enum import Enum
import random
from math import floor

from grid import Grid
from trap import Trap
from player import Player
from pickups import randomize, add_random_pickup
from item import Item
from direction import Direction
from bomb import Bomb

from gamestate import GameState
from input import Input


class Input(Enum):
    """
    Allowed input keys
    """

    NORTH = "w"
    EAST = "d"
    SOUTH = "s"
    WEST = "a"
    INVENTORY = "i"
    QUIT = "q"
    EXIT = "x"
    JUMP = "j"
    BOMB = "b"
    TRAP = "t"

    def __str__(self):
        return self.value.upper()


class GameState(Enum):
    """
    Game state for if the game is currently active, if the player stopped the game or if the player lost.
    """

    ACTIVE = "ACTIVE"
    QUIT = "QUIT"
    LOSS = "LOSS"


class Game:
    """
    Game controls the logic and rules for the game.
    """

    def __init__(self):
        """Initialize the game."""
        g = Grid()
        width, height = g.size()
        assert width > 10
        assert height > 10
        g.make_walls()

        dx = 2
        dy = 2
        mid_x = floor(width / 2)
        mid_y = floor(height / 2)
        x = 0
        y = 0
        while not g.is_empty(x, y):
            x = random.randint(mid_x - dx, mid_x + dx)
            y = random.randint(mid_y - dy, mid_y + dy)
        player = Player(x, y)
        g.set_player(player)

        randomize(g)

        x = 0
        y = 0
        while not g.is_empty(x, y):
            x = random.randint(0, width)
            y = random.randint(0, height)

        g.set_trap(x, y)

        self.grid = g
        self.player = player
        self.score = 0
        self.state = GameState.ACTIVE
        self.turn = 0
        self.refresh_rate = 25
        self.bombs = []

    def place_bomb(self):
        """
        Allows placement of a bomb at player position.
        """
        bomb = Bomb(self.player.pos_x, self.player.pos_y)
        self.bombs.append(bomb)

    def disarm_trap(self):
        """
        Disarm any trap at the player position, or on the 8 neighboring grid units.
        """
        x, y = self.player.pos_x, self.player.pos_y

        x_min = max(0, x - 1)
        y_min = max(0, y - 1)

        x_max = min(x + 1, self.grid.width)
        y_max = min(y + 1, self.grid.height)

        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                if self.grid.is_trap(x, y):
                    self.grid.clear(x, y)

    def check_bombs(self):
        """
        Check all bombs in the game to determine if any bomb is about to explode.
        """
        index_to_remove = -1
        for index in range(len(self.bombs)):
            bomb: Bomb = self.bombs[index]
            if bomb.is_exploding():
                index_to_remove = index
            else:
                bomb.tic()

        if index_to_remove == -1:
            return
        bomb = self.bombs[index_to_remove]
        print("KABOOM!")
        self.bombs.remove(bomb)

        self.grid.clear(bomb.x, bomb.y)

        x_min = max(0, bomb.x - 1)
        y_min = max(0, bomb.y - 1)

        x_max = min(bomb.x + 1, self.grid.width)
        y_max = min(bomb.y + 1, self.grid.height)
        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                self.grid.destroy(x, y)
        if self.player.pos_x < x_min or x_max < self.player.pos_x:
            return

        if self.player.pos_y < y_min or y_max < self.player.pos_y:
            return

        self.state = GameState.LOSS

    def move_player(self, direction: Direction):
        """Move the player on the grid in the direction\n
        direction = the direction to move the player"""
        dir = direction.value
        old_x = self.player.pos_x
        old_y = self.player.pos_y
        new_x = old_x + dir[0]
        new_y = old_y + dir[1]
        inside_grid = self.grid.boundary_check(new_x, new_y)
        if not inside_grid:
            print("I cannot move outside of the map")
            return

        new_pos = (new_x, new_y)
        if not self.player.can_move(direction, self.grid):
            unit = self.grid.get(new_pos[0], new_pos[1])
            print(f"I cannot move {direction} because a {unit.value} is in the way.")
            return

        maybe_item = self.grid.get(new_pos[0], new_pos[1])

        is_jumping = self.player.is_jumping
        self.player.move(direction)
        self.check_bombs()

        if isinstance(maybe_item, Item):
            item = maybe_item
            self.player.add_to_inventory(item)
            self.score += item.points
            self.grid.clear(self.player.pos_x, self.player.pos_y)
        if isinstance(maybe_item, Trap):
            trap = maybe_item
            self.score += trap.points

        self.apply_lava()

        if is_jumping:
            self.move_player(direction)

    def apply_lava(self):
        """
        The floor is made of lava, walking int lava reduces the score by 1.
        """
        self.score -= 1

    def print_status(self):
        """Displays the score and the grid"""
        print("--------------------------------------")
        print(f"You have {self.score} points.")
        print(self.grid)

    def start(self):
        """
        Starts the game loop
        """
        while GameState.ACTIVE == self.state:
            self.print_status()

            commands = input(
                f"Use {Input.NORTH}{Input.EAST}{Input.SOUTH}{Input.WEST} to move, {Input.QUIT}/{Input.EXIT} to quit. "
            )
            commands = commands.casefold()
            for i in range(len(commands)):
                if self.state != GameState.ACTIVE:
                    break
                command = commands[i]

                matched = True
                match command:
                    case Input.JUMP.value:
                        self.player.activate_jump()
                    case Input.NORTH.value:
                        self.move_player(Direction.NORTH)
                    case Input.EAST.value:
                        self.move_player(Direction.EAST)
                    case Input.SOUTH.value:
                        self.move_player(Direction.SOUTH)
                    case Input.WEST.value:
                        self.move_player(Direction.WEST)
                    case Input.INVENTORY.value:
                        inventory = self.player.get_inventory()
                        if len(inventory) == 0:
                            print("You have no items.")
                        else:
                            inventory_list = "Your inventory consists of: "
                            inventory_list += "".join(
                                [f"{item.name}, " for item in inventory]
                            )
                            inventory_list = inventory_list.rstrip(", ")
                            print(f"{inventory_list}")
                    case Input.EXIT.value:
                        self.state = GameState.QUIT
                        break
                    case Input.QUIT.value:
                        self.state = GameState.QUIT
                        break
                    case Input.BOMB.value:
                        self.place_bomb()
                    case Input.TRAP.value:
                        self.disarm_trap()
                    case _:
                        matched = False

                if matched:
                    self.turn += 1

                if self.turn % self.refresh_rate == 0:
                    add_random_pickup(self.grid)

        if GameState.QUIT == self.state:
            print(f"Thank you for playing. Your score: {self.score}")
        elif GameState.LOSS == self.state:
            print(f"Thank you for playing. You lost the game. Your score: {self.score}")
