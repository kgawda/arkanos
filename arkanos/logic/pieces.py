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

    def act(self, can_move_to):
        pass

    def move_piece(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y


class ControlledPiece(Piece):
    def __init__(self, name, x, y, controller):
        super().__init__(name, x, y)
        self.controller = controller

    def act(self, can_move_to):
        action_type, xy = self.controller.select_action()
        if action_type == 'pass':
            pass
        elif action_type == "move":
            x, y = xy
            new_x = self.x + x
            new_y = self.y + y
            if can_move_to(new_x, new_y):
                self.move_piece(*xy)
        else:
            raise Exception("Unsupported action")
