from pytest import fixture
import random

from arkanos.game.logic.engine import Engine
from arkanos.game.logic.pieces import Piece

@fixture
def engine():
    return Engine(60, 20)

@fixture
def piece():
    return Piece("Example", 0, 0)

# @fixture
# def engine_with_piece(engine, piece):
#     engine.pieces.append(piece)
#     return engine

# to samo, ale z fazą celanup:
@fixture
def engine_with_piece(engine, piece):
    engine.pieces.append(piece)
    yield engine
    engine.pieces.remove(piece)

def test_engine_creation(engine):
    assert engine.width == 60
    assert engine.height == 20
    assert not engine.pieces

def test_pieces_at(engine_with_piece):
    assert len(list(engine_with_piece.pieces_at(0, 0))) == 1


# definiujemy specjalną klasę, żeby uzyskać obiekt udający funkcję,
# który będzie zwracał na zmianę różne wartości
class MockRandrange:
    def __init__(self):
        self.step = 0
        self.results = [3, 4]
    def __call__(self, *args, **kwargs):
        result = self.results[self.step]
        self.step += 1
        self.step %= len(self.results)
        return result

@fixture
def monkeypatch_randrange(monkeypatch):
    monkeypatch.setattr(random, "randrange", MockRandrange())

def test_random_place(engine, piece, monkeypatch_randrange):
    engine.add_piece_in_random_place(piece)
    assert piece.x == 3
    assert piece.y == 4
