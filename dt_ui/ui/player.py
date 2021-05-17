from stubs.tetris_game import TetrisGame


class Player:

    def __init__(self, game: TetrisGame):
        self._game = game

    def move_left(self):
        print(self._game.move_left())

    def exit(self):
        self._game.exit()

    def run(self):
        self.move_left()
        self.exit()
