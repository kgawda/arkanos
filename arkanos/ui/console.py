from logic.engine import Engine

class ConsolePrinter:
    def __init__(self, game_engine: Engine):
        self.engine: Engine = game_engine

    def print(self):
        for y in range(self.engine.height - 1, -1, -1):
            for x in range(self.engine.width):
                pieces = list(self.engine.pieces_at(x, y))
                if pieces:
                    character = pieces[0].one_character()
                else:
                    character = '.'
                print(character, end='')
            print()
