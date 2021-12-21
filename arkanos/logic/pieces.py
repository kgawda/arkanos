class Piece:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def is_at_xy(self, x, y) -> bool:
        """Sprawdza czy ten pionek jest
        na współrzędnych x, y"""
        return self.x == x and self.y == y

    def one_character(self):
        return self.name[0]

    def act(self):
        pass


class ControlledPiece(Piece):
    def __init__(self, name, x, y, controller):
        super().__init__(name, x, y)
        self.controller = controller

    def act(self):
        action_type, xy = self.controller.select_action()
        if action_type == 'pass':
            pass
        else:
            raise Exception("Unsupported action")
