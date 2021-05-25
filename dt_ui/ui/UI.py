import pygame

# from Jogo import Jogo
# from Piece import Piece
# from Tabuleiro import Tabuleiro

play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per blo ck

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]


# adicionando restantes tipos de peças


S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]


class UI:
    def __init__(self, window, top_left_x, top_left_y, game):
        self._player = None
        self._window = window
        self.s_width = 800
        self.s_height = 700
        self._top_left_x = top_left_x
        self._top_left_y = top_left_y
        self._game = game

    @property
    def window(self):
        return self._window

    @property
    def top_left_x(self):
        return self._top_left_y

    @property
    def top_left_y(self):
        return self._top_left_y

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        print("dwqdqwdqwd")
        print(player)
        self._player = player

    def fill(self):
        self.window.fill((0, 0, 0))

    def draw_text_middle(self, text, size, color):

        font = pygame.font.SysFont('comicsans', size, bold=True)
        label = font.render(text, 1, color)

        self.window.blit(label, (
            self.top_left_x + 150 + play_width / 2 - (label.get_width() / 2),
            self.top_left_y + play_height / 2 - label.get_height() / 2))

    def draw_grid(self, row, col):
        sx = self.top_left_x + 150
        sy = self.top_left_y
        for i in range(row):
            pygame.draw.line(self.window, (0, 128, 128), (sx, sy + i * 30),
                             (sx + play_width, sy + i * 30))  # horizontal lines
            for j in range(col):
                pygame.draw.line(self.window, (0, 128, 128), (sx + j * 30, sy),
                                 (sx + j * 30, sy + play_height))  # vertical lines

    def update_score(self):
        font = pygame.font.SysFont('comicsans', 30)
        font2 = pygame.font.SysFont('comcsans', 20)

        label = font.render(self._player.name, 1, (255, 255, 255))
        label2 = font2.render(str(self._player.points) + " points", 1, (255, 255, 255))

        sx = self.top_left_x - 50
        sy = self.top_left_y + play_height / 2 - 50

        self.window.blit(label, (sx + 10, sy - 70))
        self.window.blit(label2, (sx + 10, sy - 40))


    def draw_next_shape(self, shape):
        font = pygame.font.SysFont('comicsans', 30)
        label = font.render('Next Shape', 1, (255, 255, 255))

        sx = self.top_left_x + 150 + play_width + 50
        sy = self.top_left_y + play_height / 2 - 100
        format_shape = shape.shape[shape.rotation % len(shape.shape)]

        for i, line in enumerate(format_shape):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    pygame.draw.rect(self.window, shape.color, (sx + j * 30, sy + i * 30, 30, 30), 0)

        self.window.blit(label, (sx + 10, sy - 30))

    def draw_window(self, grid):
        self.window.fill((0, 0, 0))
        # Tetris Title
        font = pygame.font.SysFont('comicsans', 60)
        label = font.render('TETRIS', 1, (255, 255, 255))

        self.window.blit(label, (self.top_left_x + 150 + play_width / 2 - (label.get_width() / 2), 30))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                pygame.draw.rect(self.window, grid[i][j], (self.top_left_x + 150 + j * 30, self.top_left_y + i * 30, 30, 30), 0)

        # draw grid and border
        self.draw_grid(40, 10)
        pygame.draw.rect(self.window, (255, 0, 0), (self.top_left_x + 150, self.top_left_y, play_width, play_height), 5)

    def draw_title(self, text, size, color):
        font = pygame.font.SysFont('comicsans', size, bold=True)
        label = font.render(text, 1, color)

        self._window.blit(label, (
            self._top_left_x + play_width / 2 - (label.get_width() / 2),
            self._top_left_y - 100 + play_height / 2 - label.get_height() / 2))

    def run(self):

        change_piece = False
        run = True
        current_piece = self._game.get_shape()
        next_piece = self._game.get_shape()

        clock = pygame.time.Clock()
        fall_time = 0
        fall_speed = 0.27
        score = 0

        while run:
            grid = self._game.create_grid()
            locked_positions = self._game.get_locked_positions()

            fall_time += clock.get_rawtime()
            clock.tick()

            # PIECE FALLING CODE
            if fall_time / 1000 >= fall_speed:
                fall_time = 0
                current_piece.y += 1
                if not (self._game.valid_space(current_piece)) and current_piece.y > 0:
                    current_piece.y -= 1
                    change_piece = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.display.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        current_piece.x -= 1
                        if not self._game.valid_space(current_piece):
                            current_piece.x += 1

                    elif event.key == pygame.K_RIGHT:
                        current_piece.x += 1
                        if not self._game.valid_space(current_piece):
                            current_piece.x -= 1

                    elif event.key == pygame.K_UP:
                        # rotate shape
                        current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                        if not self._game.valid_space(current_piece):
                            current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)

                    if event.key == pygame.K_DOWN:
                        # move shape down
                        current_piece.y += 1
                        if not self._game.valid_space(current_piece):
                            current_piece.y -= 1

            shape_pos = self._game.convert_shape_format(current_piece)

            # add piece to the grid for drawing
            for i in range(len(shape_pos)):
                x, y = shape_pos[i]
                if y > -1:
                    grid[y][x] = current_piece.color

            # IF PIECE HIT GROUND
            if change_piece:
                for pos in shape_pos:
                    p = (pos[0], pos[1])
                    locked_positions[p] = current_piece.color
                self._game.set_locked_positions(locked_positions)
                current_piece = next_piece
                next_piece = self._game.get_shape()
                change_piece = False

                score_plus = self._game.clear_rows(grid)
                print("ola ", score_plus)
                # call four times to check for multiple clear rows
                if score_plus:
                    self._player.points = score_plus
                    self.update_score()

            self.draw_window(grid)
            self.draw_next_shape(next_piece)
            self.update_score()
            pygame.display.update()

            # Check if user lost
            if self._game.check_lost():
                run = False

        self.draw_text_middle("You Lost", 40, (255, 255, 255))
        pygame.display.update()
        pygame.time.delay(2000)
