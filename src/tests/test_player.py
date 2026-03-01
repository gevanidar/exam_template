import unittest
from grid import Grid
from unit import Unit
from player import Player


class TestGrid(unittest.TestCase):
    def test_player_move_into_an_obstacle(self):
        """Tests if a player can move into an obstacle"""
        player = Player(2, 1)
        g = Grid()
        x = 2
        y = 2
        g.set(x, y, Unit.WALL)
        g.set_player(player)

        moved = player.can_move(2, 2, g)

        self.assertEqual(False, moved)
