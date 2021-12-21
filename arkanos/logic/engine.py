import random
from typing import List, Generator

from logic.pieces import Piece, ControlledPiece


class Engine:
    def __init__(self, width, height):
        self.width: int = width
        self.height: int = height
        self.pieces: List[Piece] = []

    def add_piece_in_random_place(self, piece: Piece):
        piece.x = random.randrange(self.width)
        piece.y = random.randrange(self.height)
        self.pieces.append(piece)

    def pieces_at(self, x, y) -> Generator[Piece, None, None]:
        """Zwraca iterator po wszystkich pionkach znajdujących się
        na współrzędnych x, y"""
        for piece in self.pieces:
            if piece.is_at_xy(x, y):
                yield piece

    def play_round(self):
        for piece in self.pieces:
            #if isinstance(piece, ControlledPiece):
            piece.act()
