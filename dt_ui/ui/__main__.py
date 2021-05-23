import stubs
import ui
from stubs.tetris_game import TetrisGame
from ui.Button import Button
from ui.TextInput import TextBox
from ui.UI import UI
from ui.Player import Player
import pygame

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

done = False

play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per blo ck
# screen resolution

pygame.font.init()
# GLOBALS VARS

widgets = []

entry_settings = {
    "inactive_on_enter": False,
    'active': False
}


def textbox_callback(id, final):
    print('enter pressed, textbox contains {}'.format(final))


def alternative_callback(id, final):
    print('alternative textbox contains {}'.format(final))


def button_callback():
    global done
    done = True


def main_menu():

    game = TetrisGame(ui.SERVER_ADDRESS, stubs.PORT)  # STUB
    # see all settings help(pygooey.TextBox.__init__)

    ui_game = UI(pygame.display.set_mode((800, 700)), (800 - play_width) // 2, 700 - play_height)

    global done

    entry = TextBox(rect=(320, 450, 150, 30), command=textbox_callback, **entry_settings)

    widgets.append(entry)

    # see all settings help(pygooey.Button.__init__)
    btn_settings = {
        "clicked_font_color": (0, 0, 0),
        "hover_font_color": (205, 195, 100),
        'font': pygame.font.Font(None, 16),
        'font_color': (255, 255, 255),
        'border_color': (0, 0, 0),
    }

    btn = Button(rect=(320, 550, 150, 50), command=button_callback, text='JOGAR', **btn_settings)
    widgets.append(btn)

    ui_game.draw_title('DISTRIBUTED TETRIS', 55, (255, 255, 255))

    ui_game.draw_text_middle('Insert Player', 35, (255, 255, 255))

    while not done:
        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.K_RETURN or event.type == pygame.QUIT:
                done = True
            for w in widgets:
                w.get_event(event)
        for w in widgets:
            w.update()
            w.draw(ui_game.window)
        pygame.display.update()

    run = True
    while run:
        ui_game.fill()
        ui_game.draw_text_middle('Press any key to begin.', 60, (255, 255, 255))
        name = ""
        for caracter in entry.buffer:
            name += caracter
        p = Player(name, game)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                ui_game.run(p)
    pygame.quit()


pygame.display.set_caption('Tetris')

main_menu()  # start game
