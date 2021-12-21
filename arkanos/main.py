from logic.pieces import Piece, ControlledPiece
from logic.engine import Engine
from ui.console import ConsolePrinter
from bots.simple import DoNotihngBot


def main() -> None:
    # Żeby mypy sprawdził tę funkcę:
    # - annotacja typu zwracanego, lub
    # - mypy arkanos --check-untyped-defs
    engine = Engine(80, 10)
    printer = ConsolePrinter(engine)
    drzewo = Piece("Drzewo", 0, 0)
    player1_controller = DoNotihngBot()
    player1 = ControlledPiece("Arkanos", 0, 0, player1_controller)
    # player2 = Piece("Barbarios", 0, 0)
    engine.add_piece_in_random_place(player1)
    engine.add_piece_in_random_place(drzewo)
    for p in engine.pieces:
        print(f"  {p.name} ({p.x}, {p.y})")

    printer.print()
    print()
    engine.play_round()
    printer.print()


if __name__ == '__main__':
    main()
