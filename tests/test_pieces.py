from pytest import raises

from arkanos.game.logic.pieces import Piece, ControlledPiece

def test_piece_creation():
    p = Piece("Name", 1, 2)
    assert p.name == "Name"
    assert p.x == 1
    assert p.y == 2

    with raises(ValueError):
        Piece("", 1, 2)

def test_piece_display():
    p = Piece("Name", 1, 2)
    assert p.one_character() == "N"


