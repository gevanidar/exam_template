import unittest
from grid import Grid, Unit


class TestGrid(unittest.TestCase):
    def test_position_does_contain_an_obstacle(self):
        """Tests if position does contain an obstacle"""
        g = Grid()
        x = 2
        y = 2
        g.set(x, y, Unit.WALL)
        is_obstacle = g.is_obstacle(x, y)

        self.assertEqual(True, is_obstacle)

    def test_position_does_not_contain_an_obstacle(self):
        """Tests if position does not contain an obstacle"""
        g = Grid()
        x = 2
        y = 2
        g.clear(x, y)
        is_obstacle = g.is_obstacle(x, y)

        self.assertEqual(False, is_obstacle)
