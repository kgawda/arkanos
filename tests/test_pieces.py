from pytest import raises, fixture, mark, fail

from arkanos.game.logic.pieces import Piece, ControlledPiece, FightingPiece


@fixture
def example_piece():
    return Piece("Name", 1, 2)

def test_piece_creation(example_piece):
    assert example_piece.name == "Name"
    assert example_piece.x == 1
    assert example_piece.y == 2

    with raises(ValueError):
        Piece("", 1, 2)

def test_piece_display(example_piece):
    assert example_piece.one_character() == "N"


@mark.parametrize("power1,power2,result", [
    (51, 50, True),
    (50, 51, False),
    (50, 50, True)
])
def test_fight(power1, power2, result):
    p1 = FightingPiece("Wojownik1", 0, 0, health=100, power=power1)
    p2 = FightingPiece("Wojownik2", 0, 0, health=100, power=power2)
    assert p1.fight(p2) == result

@mark.xfail
def test_to_nie_zadziala(engine):
    engine.add_piece_in_random_place(123)
