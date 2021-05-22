import pygame

from UI import UI


"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block

pygame.font.init()
# GLOBALS VARS


def main_menu():
    ui = UI(pygame.display.set_mode((800, 700)), (800 - play_width) // 2, 700 - play_height)
    run = True
    while run:
        ui.fill()
        ui.draw_text_middle('Press any key to begin.', 60, (255, 255, 255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                ui.run()
    pygame.quit()


pygame.display.set_caption('Tetris')

main_menu()  # start game
