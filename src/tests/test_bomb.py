"""Module testing the Bomb class."""

import unittest
from ..bomb import Bomb


class TestBomb(unittest.TestCase):
    """Test class for the Bomb class."""

    def test_bomb_explosion(self):
        """Test if the bomb explodes after 3 turns."""
        bomb = Bomb(0, 0)

        self.assertEqual(False, bomb.is_exploding())

        bomb.tic()
        bomb.tic()
        bomb.tic()
        self.assertEqual(True, bomb.is_exploding())
