from stubs.tetris_game import TetrisGame


class Player:

################## adicionados atributos necessários para o jogador ##################

    #name = ''
    #points = 0
    #active = False
#######################################################################################


    def __init__(self, name, game: TetrisGame):
        self._game = game
        self._name = name
        self._points = 0
        self._active = True


# adicionados métodos para os INPUTS do jogo

    def move_left(self):
        print(self._game.move_left())

    def move_right(self):
        print(self._game.move_right())

    def move_down(self):
        print(self._game.move_down())

    def move_up(self):
        print(self._game.move_up())

    def exit(self):
        self._game.exit()

    def run(self):
        self.move_left()
        self.exit()

    @property
    def name(self):
        return self._name

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, points):
        self._points += points


######################################################################


    # set player points

    def setPoints(self):
        self.points += 1

    # reset pontuaçoes no fim do jogo

    def resetPoints(self):
        self.points = 0

########################################################################


