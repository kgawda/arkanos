import time

from game.logic.pieces import Piece, ControlledPiece
from game.logic.engine import Engine
from game.ui.console import ConsolePrinter
from game.bots.simple import DoNotihngBot, RandomWalk


def main() -> None:
    # Żeby mypy sprawdził tę funkcę:
    # - annotacja typu zwracanego, lub
    # - mypy arkanos --check-untyped-defs
    engine = Engine(80, 8)
    printer = ConsolePrinter(engine)
    drzewo = Piece("Drzewo", 0, 0)
    player1_controller = RandomWalk()
    player1 = ControlledPiece("Arkanos", 0, 0, player1_controller)
    # player2 = Piece("Barbarios", 0, 0)
    engine.add_piece_in_random_place(player1)
    engine.add_piece_in_random_place(drzewo)
    for p in engine.pieces:
        print(f"  {p.name} ({p.x}, {p.y})")

    # import objgraph
    # objgraph.show_backrefs(player1_controller, filename='backrefs.png', max_depth=8)
    # objgraph.show_refs(printer, filename='refs.png', max_depth=8)

    while True:
        engine.play_round()
        printer.print()
        time.sleep(0.2)


if __name__ == '__main__':
    main()
    # import greet
    # greet.greet("Arkanos")