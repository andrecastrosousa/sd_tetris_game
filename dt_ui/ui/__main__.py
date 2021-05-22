import stubs
import ui
from stubs.tetris_game import TetrisGame
from ui.player import Player


def main():

    game = TetrisGame(ui.SERVER_ADDRESS, stubs.PORT) # STUB

    player = Player("game",game)
    player.run()

main()