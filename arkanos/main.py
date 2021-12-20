from logic.pieces import Piece
from logic.engine import Engine


def main():
    engine = Engine(80, 20)
    player1 = Piece("Arkanos", 0, 0)
    engine.add_piece_in_random_place(player1)
    for p in engine.pieces:
        print(f"  {p.name} ({p.x}, {p.y})")


if __name__ == '__main__':
    main()
