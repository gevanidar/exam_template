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

        randomize(g)

        # Randomize trap position on grid
        x, y = g.randomized_empty_position(0, 0, width - 1, height - 1)
        g.set_trap(x, y)

        # Randomize player position to middle
        dx = 2
        dy = 2
        mid_x = floor(width / 2)
        mid_y = floor(height / 2)
        x, y = g.randomized_empty_position(
            mid_x - dx, mid_y - dy, mid_x + dx, mid_y + dy
        )
        player = Player(x, y)
        g.set_player(player)

        self.grid = g
        self.player = player
        self.score = 0
        self.state = GameState.ACTIVE
        self.turn = 0
        self.refresh_rate = 25

    def place_bomb(self):
        """
        Allows placement of a bomb at player position.
        """
        bomb = Bomb(self.player.pos_x, self.player.pos_y)
        self.grid.put_bomb(bomb)

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
        self.grid.tic_bombs()

        bomb = self.grid.explode_bomb()
        if not bomb:
            return

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
        print(f"You have {self.score} points.")
        print(self.grid)

    def start(self):
        """
        Starts the game loop
        """
        while GameState.ACTIVE == self.state:
            self.print_status()

            commands = input(
                f"Use {Input.MOVE_NORTH}{Input.MOVE_EAST}{Input.MOVE_SOUTH}{Input.MOVE_WEST} to move, {Input.QUIT_GAME}/{Input.EXIT_GAME} to quit.\n"
                + f'Commands will execute in succession, "{Input.MOVE_NORTH.value}{Input.MOVE_NORTH.value}{Input.MOVE_EAST.value}" then the player will {Input.MOVE_NORTH.description()} twice then {Input.MOVE_EAST.description()} once (if possible).\n'
                + f"{Input.SHOW_HELP.explanation()}.\n"
                + "Your commands: "
            )
            commands = commands.casefold()
            print("--------------------------------------")
            print(f"Log from executing {commands}:")
            for i in range(len(commands)):
                if self.state != GameState.ACTIVE:
                    break
                command = commands[i]

                matched = True
                match command:
                    case Input.ACTIVATE_JUMP.value:
                        self.player.activate_jump()
                    case Input.MOVE_NORTH.value:
                        self.move_player(Direction.NORTH)
                    case Input.MOVE_EAST.value:
                        self.move_player(Direction.EAST)
                    case Input.MOVE_SOUTH.value:
                        self.move_player(Direction.SOUTH)
                    case Input.MOVE_WEST.value:
                        self.move_player(Direction.WEST)
                    case Input.SHOW_INVENTORY.value:
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
                    case Input.EXIT_GAME.value:
                        self.state = GameState.QUIT
                        break
                    case Input.QUIT_GAME.value:
                        self.state = GameState.QUIT
                        break
                    case Input.PLACE_BOMB.value:
                        self.place_bomb()
                    case Input.DISARM_TRAP.value:
                        self.disarm_trap()
                    case Input.SHOW_HELP.value:
                        instructions = "All keys and their function:"
                        for i in Input:
                            instructions += "\n"
                            instructions += i.explanation()
                        print(instructions)

                    case _:
                        print(f"The key '{command}' has no use here.")
                        matched = False

                if matched:
                    self.turn += 1

                if self.turn % self.refresh_rate == 0:
                    add_random_pickup(self.grid)

        if GameState.QUIT == self.state:
            print(f"Thank you for playing. Your score: {self.score}")
        elif GameState.LOSS == self.state:
            print(f"Thank you for playing. You lost the game. Your score: {self.score}")
