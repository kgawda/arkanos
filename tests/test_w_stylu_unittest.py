import unittest

from arkanos.game.logic.pieces import Piece


class TestPieces(unittest.TestCase):

    def test_piece_creation(self):
        p = Piece("Name", 1, 2)
        self.assertEqual(p.name, "Name")
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)
