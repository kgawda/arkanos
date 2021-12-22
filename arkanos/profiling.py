import timeit
import cProfile
import pstats

import simulator
from game.logic.pieces import Piece
from game.logic.engine import Engine

def main():

    # python -m timeit "33**33"

    print(timeit.timeit('sum(range(1000))', number=1000)/1000)
    print(timeit.repeat('sum(range(1000))', number=1000, repeat=3))

    engine = Engine(80, 8)
    for _ in range(10):
        p = Piece("Testowy", 0, 0)
        engine.add_piece_in_random_place(p)

    print(timeit.timeit(lambda: list(engine.pieces_at(0, 0)), number=1000)/1000)
    print(timeit.timeit(simulator.main, number=10) / 10)

    # python -m cProfile -s cumulative arkanos\simulator.py

    cProfile.run('simulator.main()', filename='result.pstats')
    s = pstats.Stats('result.pstats')
    s.sort_stats('cumulative')
    s.print_stats()

    print("=== context manager ===")

    with cProfile.Profile() as pr:
        engine.pieces_at(0, 0)
        engine.pieces[0].act(engine.can_move_to)

    pr.print_stats()


if __name__ == '__main__':
    main()
