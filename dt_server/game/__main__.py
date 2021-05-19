import game
import skeletons



def main():
    skeletons.TetrisServer(skeletons.PORT, game.TetrisServer()).run()

main()
