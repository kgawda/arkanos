import timeit
import cProfile
import pstats
import sys

import objgraph

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

    # tylko Linux:
    # pip install statprof-smarkets
    # python -m statprof simulator.py
    #    albo
    # with statprof.profile():
    #     ...

    ############## RAM ################

    b = sys.getsizeof(Piece("Test", 0, 0))
    print(f"Piece zajmuje {b} bajtów")

    b = sys.getsizeof("")
    print(f"Pusty str zajmuje {b} bajtów")

    b = sys.getsizeof("1234")
    print(f"Str 4-literowy zajmuje {b} bajtów")


    # Tylko na Linux:
    # import resource as r
    # r.getusage(r.RUSAGE_SELF).ru_maxrss # w kilobajtach

    # użycie __slots__ --> obiekty klasy B nie będą miały __dict__
    # --> trochę szybszy dostęp i 8 B pamięci mniej zużyte
    class B:
        __slots__ = ('x',)
        def __init__(self, x):
            self.x = x

    # tymczasowy problem - trzeba doinstalować graphviz osobno:
    #   https://graphviz.org/download/
    # pip install objgraph
    # --> użycie pokazane w main.py


if __name__ == '__main__':
    main()
