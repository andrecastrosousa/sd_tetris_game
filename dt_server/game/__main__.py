import game
import skeletons
from game.Jogo import Jogo
from game.Tabuleiro import Tabuleiro


def main():
    jogo = Jogo(Tabuleiro(), game.shapes)
    skeletons.TetrisServer(skeletons.PORT, jogo).run()


main()
