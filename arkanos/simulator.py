import io

from game.logic.pieces import Piece, ControlledPiece
from game.logic.engine import Engine
from game.ui.console import ConsolePrinter
from game.bots.simple import DoNotihngBot, RandomWalk

def main() -> None:
    engine = Engine(80, 8)
    printer = ConsolePrinter(engine)
    for _ in range(10):
        p = ControlledPiece("Testowy", 0, 0, RandomWalk())
        engine.add_piece_in_random_place(p)

    output = io.StringIO()
    for _ in range(100):
        engine.play_round()
        printer.print(out=output)

if __name__ == '__main__':
    main()
