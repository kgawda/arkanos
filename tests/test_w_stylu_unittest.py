import unittest

from arkanos.game.logic.pieces import Piece


class TestPieces(unittest.TestCase):
    def setUp(self) -> None:
        self.p = Piece("Name", 1, 2)

    def test_piece_creation(self):
        self.assertEqual(self.p.name, "Name")
        self.assertEqual(self.p.x, 1)
        self.assertEqual(self.p.y, 2)

    # def tearDown(self) -> None:
    #     self.p.die()
