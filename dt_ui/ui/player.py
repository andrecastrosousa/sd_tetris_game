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


    def move_left(self):
        print(self._game.move_left())

    def exit(self):
        self._game.exit()

    def run(self):
        self.move_left()
        self.exit()


######################################################################


    # set player points

    def setPoints(self):
        self.points += 1

    # reset pontuaçoes no fim do jogo

    def resetPoints(self):
        self.points = 0

########################################################################


