

from dt_ui.ui import player


class TetrisServer:

    @staticmethod
    def left():
        return "left"

    @staticmethod
    def right():
        return "right"



    # lista de jogadores

    player_list = []

    # adicionar jogadores

    def addPlayer(name):
        player = Player(name)
        player_list.__add__(player)
