import stubs
import ui
from stubs.tetris_game import TetrisGame
from ui.player import Player


def main():
    game = TetrisGame(ui.SERVER_ADDRESS, stubs.PORT)

    player = Player(game)
    player.run()

main()