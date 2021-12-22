class Piece:
    def __init__(self, name, x, y, *args, **kwargs):
        # print("init Piece")
        if not name:
            raise ValueError("Piece name cannot be empty")
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
        """Moves piece by given deltas.
        Example:
        >>> p = Piece("test", 0, 0)
        >>> p.move_piece(1, 1)
        >>> p.x
        1
        """
        self.x += delta_x
        self.y += delta_y


class ControlledPiece(Piece):
    def __init__(self, name, x, y, controller, *args, **kwargs):
        # print("init ControlledPiece")
        super().__init__(name, x, y, *args, **kwargs)
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

class FightingPiece(Piece):
    def __init__(self, name, x, y, health, power, *args, **kwargs):
        # print("init FightingPiece")
        super().__init__(name, x, y, *args, **kwargs)
        self.health = health
        self.power = power

    def fight(self, other):
        if not isinstance(other, FightingPiece):
            return
        if self.power >= other.power:
            winner = self
            looser = other
        else:
            winner = other
            looser = self
        winner.power += 1
        looser.health = 0
        return winner == self


class ControlledFightingPiece(ControlledPiece, FightingPiece):
    pass

# ControlledFightingPiece.__mro__ :
# (<class 'arkanos.logic.pieces.ControlledFightingPiece'>, <class 'arkanos.logic.pieces.ControlledPiece'>, <class 'arkanos.logic.pieces.FightingPiece'>, <class 'arkanos.logic.pieces.Piece'>, <class 'object'>)

# ControlledFightingPiece("Name", 0, 0, controller=None, health=100, power=50)
