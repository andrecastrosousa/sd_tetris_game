from stubs.tetris_game import TetrisGame


class Player:

# adicionados atributos necessários para o jogador

    name = ''
    points = 0
    active = False


    def __init__(self, game: TetrisGame):
        self._game = game

    def move_left(self):
        print(self._game.move_left())

    def exit(self):
        self._game.exit()

    def run(self):
        self.move_left()
        self.exit()


######################################################################

    # set player name

    def setName(self, name):
        self.name = name

    # set player points

    def setPoints(self):
        self.points += 1




