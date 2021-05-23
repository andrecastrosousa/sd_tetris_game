

from dt_ui.ui import Player


class TetrisServer:

    @staticmethod
    def left():
        return "left"

    @staticmethod
    def right():
        return "right"

    # adicionados métodos em falta

    @staticmethod
    def down():
        return "down"

    @staticmethod
    def up():
        return "up"



    # lista de jogadores

    player_list = []

    # adicionar jogadores

    def addPlayer(name):
        player = Player(name)
        player_list.__add__(player)

    # trocar de jogador quando completa uma linha ou assenta a peça

    def switchPlayer(self):
        if player_list[0].active == False:
            player_list[0].active = True
        else:
            player_list[1] = True