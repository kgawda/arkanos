class Piece:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def is_at_xy(self, x, y) -> bool:
        """Sprawdza czy ten pionek jest
        na współrzędnych x, y"""
        return self.x == x and self.y == y
