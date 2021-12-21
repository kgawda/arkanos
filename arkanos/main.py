from logic.pieces import Piece
from logic.engine import Engine
from ui.console import ConsolePrinter


def main() -> None:
    # Żeby mypy sprawdził tę funkcę:
    # - annotacja typu zwracanego, lub
    # - mypy arkanos --check-untyped-defs
    engine = Engine(80, 20)
    printer = ConsolePrinter(engine)
    player1 = Piece("Arkanos", 0, 0)
    # player2 = Piece("Barbarios", 0, 0)
    engine.add_piece_in_random_place(player1)
    for p in engine.pieces:
        print(f"  {p.name} ({p.x}, {p.y})")

    printer.print()

if __name__ == '__main__':
    main()
