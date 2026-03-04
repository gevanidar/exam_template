"""Module for testing the Player class."""

import unittest
from ..grid import Grid
from ..unit import Unit
from ..player import Player
from ..item import Item
from ..direction import Direction


class TestPlayer(unittest.TestCase):
    """Player test class, used for testing player functionality."""

    def test_player_move_into_an_obstacle(self):
        """Tests if a player can move into an obstacle."""
        player = Player(2, 1)
        g = Grid()
        x = 2
        y = 2
        g.set(x, y, Unit.WALL)
        g.set_player(player)

        moved = player.can_move(Direction.SOUTH, g)

        self.assertEqual(False, moved)

    def test_player_pickup_item(self):
        """Test is player can pickup an item."""
        player = Player(2, 1)
        self.assertEqual(0, len(player.inventory.items))
        item = Item("carrot")
        player.add_to_inventory(item)
        self.assertEqual(1, len(player.inventory.items))
        self.assertEqual(item, player.inventory.get(0))
