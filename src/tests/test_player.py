import unittest
from grid import Grid, Unit
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

        moved = player.move(0, 1)

        self.assertEqual(False, moved)
