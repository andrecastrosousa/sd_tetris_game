import pygame

from Button import Button
from Player import Player
from TextInput import TextBox
from UI import UI


"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

done = False


play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per blo ck
# screen resolution
res = (720, 720)

# opens up a window
screen = pygame.display.set_mode(res)

# white color
color = (255, 255, 255)

# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

pygame.font.init()
# GLOBALS VARS

screen_rect = screen.get_rect()
done = False
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

# refactor later, copied from UI.py

def draw_text_middle(window, top_left_x, top_left_y, text, size, color):

    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)

    window.blit(label, (
        top_left_x + play_width / 2 - (label.get_width() / 2),
        top_left_y + play_height / 2 - label.get_height() / 2))

def draw_title(window, top_left_x, top_left_y, text, size, color):

    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)

    window.blit(label, (
        top_left_x + play_width / 2 - (label.get_width() / 2),
        top_left_y + play_height / 2 - label.get_height() / 2))




def main_menu():
    # see all settings help(pygooey.TextBox.__init__)

    ui = UI(pygame.display.set_mode((800, 700)), (800 - play_width) // 2, 700 - play_height)

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

    #ui.draw_text_middle('DISTRIBUTED TETRIS', 60, (0, 255, 0))

    draw_title(ui.window, ui.top_left_x, ui.top_left_y - 100,'DISTRIBUTED TETRIS', 55, (255, 255, 255))

    draw_text_middle(ui.window, ui.top_left_x, ui.top_left_y, 'Insert Player', 35, (255, 255, 255))


    while not done:
        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.K_RETURN or event.type == pygame.QUIT:
                done = True
            for w in widgets:
                w.get_event(event)
        for w in widgets:
            w.update()
            w.draw(screen)
        pygame.display.update()


    run = True
    while run:
        ui.fill()
        ui.draw_text_middle('Press any key to begin.', 60, (255, 255, 255))
        name = ""
        for caracter in entry.buffer:
            name += caracter
        p = Player(name, 0)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                ui.run(p)
    pygame.quit()


pygame.display.set_caption('Tetris')

main_menu()  # start game
