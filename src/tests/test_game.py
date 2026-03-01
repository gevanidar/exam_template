import unittest

from direction import Direction
from game import Game


class TestGrid(unittest.TestCase):
    def test_lava_on_move(self):
        """Test apply lava reducing score"""
        game = Game()
        self.assertEqual(0, game.score)
        game.apply_lava()
        self.assertEqual(-1, game.score)
        game.apply_lava()
        game.apply_lava()
        self.assertEqual(-3, game.score)
