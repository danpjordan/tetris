# Press Start 2P font by codeman38

from Assets import tetris_funct
import pygame
import os
import random
pygame.font.init()


# Defines the size, in pixels, of each square
SQUARE_SIZE = 24

# Defines the size of the buffer
BUFFER = SQUARE_SIZE // 2

# Defines the how many squares the game board is
GAME_WIDTH_SQUARES = 10
GAME_HEIGHT_SQUARES = 20

# Defines the dimentions of the game board
GAME_DISPLAY_WIDTH = 10 * SQUARE_SIZE
GAME_DISPLAY_HEIGHT = 20 * SQUARE_SIZE

# Defines the dimentions of the displays
SIDE_DISPLAY_WIDTH_RIGHT = 7 * SQUARE_SIZE
SIDE_DISPLAY_WIDTH_LEFT = 6 * SQUARE_SIZE
SIDE_DISPLAY_WIDTH_BOTTEM = 5 * SQUARE_SIZE
TOP_DISPLAY_HEIGHT = 2 * SQUARE_SIZE
STATS_DISPLAY_HEIGHT = 2 * SQUARE_SIZE + 3 * BUFFER
HOLD_DISPLAY_HEIGHT = 3 * SQUARE_SIZE + 3 * BUFFER
NEXT_DISPLAY_HEIGHT = 9 * SQUARE_SIZE + 6 * BUFFER

# Defines the dementions of the board
BOARD_WIDTH_PIXLES = 6 * BUFFER + GAME_DISPLAY_WIDTH + \
    SIDE_DISPLAY_WIDTH_LEFT + SIDE_DISPLAY_WIDTH_RIGHT
BOARD_HEIGHT_PIXLES = 5 * BUFFER + TOP_DISPLAY_HEIGHT + GAME_DISPLAY_HEIGHT

# Defines colors
WHITE = (255, 255, 255)
GRAY = (170, 170, 170)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
DARK_GRAY = (110, 110, 110)

# Defines fonts
TEXT_FONT = pygame.font.Font(os.path.join('Assets', 'press_start_2P.ttf'), 24)
GAME_OVER_FONT = pygame.font.Font(
    os.path.join('Assets', 'press_start_2P.ttf'), 34)
NUMBER_FONT = pygame.font.Font(
    os.path.join('Assets', 'press_start_2P.ttf'), 50)
PAUSE_FONT = pygame.font.Font(os.path.join('Assets', 'press_start_2P.ttf'), 14)

# Defines events
MOVE_DOWN = pygame.USEREVENT + 1
NEW_PIECE = pygame.USEREVENT + 2
GAME_OVER = pygame.USEREVENT + 3

# Defines the width and hight, in pixels, of the window
WIN = pygame.display.set_mode((BOARD_WIDTH_PIXLES, BOARD_HEIGHT_PIXLES))
pygame.display.set_caption("tetris")


FPS = 60


def draw_window():
    """Draws a blank window to the display"""

    WIN.fill(GRAY)

    LEVEL_DISPLAY = pygame.Rect(
        2 * BUFFER, 2 * BUFFER, SIDE_DISPLAY_WIDTH_LEFT, STATS_DISPLAY_HEIGHT)
    pygame.draw.rect(WIN, BLACK, LEVEL_DISPLAY)

    SCORE_DISPLAY = pygame.Rect(BOARD_WIDTH_PIXLES - (2 * BUFFER + SIDE_DISPLAY_WIDTH_RIGHT),
                                2 * BUFFER, SIDE_DISPLAY_WIDTH_RIGHT, STATS_DISPLAY_HEIGHT)
    pygame.draw.rect(WIN, BLACK, SCORE_DISPLAY)

    LINE_DISPLAY = pygame.Rect(
        3 * BUFFER + SIDE_DISPLAY_WIDTH_LEFT, 2 * BUFFER, GAME_DISPLAY_WIDTH, TOP_DISPLAY_HEIGHT)
    pygame.draw.rect(WIN, BLACK, LINE_DISPLAY)

    HOLD_DISPLAY = pygame.Rect(
        2 * BUFFER + SQUARE_SIZE, 3 * BUFFER + STATS_DISPLAY_HEIGHT, SIDE_DISPLAY_WIDTH_BOTTEM, HOLD_DISPLAY_HEIGHT)
    pygame.draw.rect(WIN, BLACK, HOLD_DISPLAY)

    NEXT_DISPLAY = pygame.Rect(BOARD_WIDTH_PIXLES - (2 * BUFFER + SIDE_DISPLAY_WIDTH_RIGHT),
                               3 * BUFFER + STATS_DISPLAY_HEIGHT, SIDE_DISPLAY_WIDTH_BOTTEM, NEXT_DISPLAY_HEIGHT)
    pygame.draw.rect(WIN, BLACK, NEXT_DISPLAY)

    GAME_DISPLAY = pygame.Rect(3 * BUFFER + SIDE_DISPLAY_WIDTH_LEFT, 3 *
                               BUFFER + TOP_DISPLAY_HEIGHT, GAME_DISPLAY_WIDTH, GAME_DISPLAY_HEIGHT)
    pygame.draw.rect(WIN, BLACK, GAME_DISPLAY)

    pygame.display.update()


def draw_box(x, y, n):
    """Draws a box on the display given the position (x, y) and color (n)"""

    if n == "*":
        color = BLACK
    elif n == "$":
        color = PURPLE
    elif n == "+":
        color = GREEN
    elif n == "-":
        color = RED
    elif n == "#":
        color = ORANGE
    elif n == "=":
        color = BLUE
    elif n == "%":
        color = YELLOW
    elif n == "@":
        color = CYAN
    else:
        color = WHITE

    outer_box = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
    pygame.draw.rect(WIN, BLACK, outer_box)
    inner_box = pygame.Rect(x + 1, y - 1, SQUARE_SIZE - 2, SQUARE_SIZE - 2)
    pygame.draw.rect(WIN, color, inner_box)


def draw_game_board(d_board):
    """Draws the game board onto the display"""

    GAME_BOARD_STARTING_WIDTH = 3 * BUFFER + SIDE_DISPLAY_WIDTH_LEFT
    GAME_BOARD_STARTING_HEIGHT = 3 * BUFFER + TOP_DISPLAY_HEIGHT
    for i in range(20):
        for j in range(10):
            draw_box(GAME_BOARD_STARTING_WIDTH + j * SQUARE_SIZE,
                     GAME_BOARD_STARTING_HEIGHT + i * SQUARE_SIZE, d_board[i][j])
    top_of_game_board = pygame.Rect(
        GAME_BOARD_STARTING_WIDTH, GAME_BOARD_STARTING_HEIGHT - 1, GAME_DISPLAY_WIDTH, 1)
    pygame.draw.rect(WIN, BLACK, top_of_game_board)

    pygame.display.update()


def draw_line_display(stats):
    """Draws the line display and updates it with how many lines the user has clearned"""

    line = stats[1]
    STARTING_LINE_TEXT_WIDTH = 4 * BUFFER + SIDE_DISPLAY_WIDTH_LEFT
    STARTING_LINE_TEXT_HEIGHT = 2 * BUFFER
    LINE_DISPLAY = pygame.Rect(
        3 * BUFFER + SIDE_DISPLAY_WIDTH_LEFT, 2 * BUFFER, GAME_DISPLAY_WIDTH, TOP_DISPLAY_HEIGHT)
    pygame.draw.rect(WIN, BLACK, LINE_DISPLAY)

    LINE_TEXT = "LINES-"
    for i, char in enumerate(LINE_TEXT):
        draw_text = TEXT_FONT.render(char, 1, WHITE)
        WIN.blit(draw_text, (STARTING_LINE_TEXT_WIDTH + i * SQUARE_SIZE,
                 STARTING_LINE_TEXT_HEIGHT + (TOP_DISPLAY_HEIGHT - draw_text.get_height()) // 2))

    line_arr = line % 10, line // 10 % 10, line // 100 % 10
    for i in range(3):
        draw_text = TEXT_FONT.render(str(line_arr[2 - i]), 1, WHITE)
        WIN.blit(draw_text, (STARTING_LINE_TEXT_WIDTH + 6 * SQUARE_SIZE + i * SQUARE_SIZE,
                 STARTING_LINE_TEXT_HEIGHT + (TOP_DISPLAY_HEIGHT - draw_text.get_height()) // 2))


def draw_score_display(stats):
    """Draws the score display and updates it with the users current score"""

    score = stats[0]
    SCORE_DISPLAY = pygame.Rect(BOARD_WIDTH_PIXLES - (2 * BUFFER + SIDE_DISPLAY_WIDTH_RIGHT),
                                2 * BUFFER, SIDE_DISPLAY_WIDTH_RIGHT, STATS_DISPLAY_HEIGHT)
    pygame.draw.rect(WIN, BLACK, SCORE_DISPLAY)

    STARTING_SCORE_TEXT_WIDTH = BOARD_WIDTH_PIXLES - \
        (2 * BUFFER + SIDE_DISPLAY_WIDTH_RIGHT) + BUFFER
    STARTING_SCORE_TEXT_HEIGHT = 3 * BUFFER
    score_text = "SCORE"
    for i, char in enumerate(score_text):
        draw_text = TEXT_FONT.render(char, 1, WHITE)
        WIN.blit(draw_text, (STARTING_SCORE_TEXT_WIDTH + i *
                 SQUARE_SIZE + BUFFER, STARTING_SCORE_TEXT_HEIGHT))

    score_arr = score % 10, score // 10 % 10, score // 100 % 10, score // 1000 % 10, score // 10000 % 10, score // 100000 % 10
    for i in range(6):
        draw_text = TEXT_FONT.render(str(score_arr[5 - i]), 1, WHITE)
        WIN.blit(draw_text, (STARTING_SCORE_TEXT_WIDTH + i * SQUARE_SIZE +
                 1, STARTING_SCORE_TEXT_HEIGHT + SQUARE_SIZE + BUFFER))


def draw_level_display(stats):
    """Draws the level display and updates it with the users level"""

    level = min(29, stats[1] // 10 + 1)

    LEVEL_DISPLAY = pygame.Rect(
        2 * BUFFER, 2 * BUFFER, SIDE_DISPLAY_WIDTH_LEFT, STATS_DISPLAY_HEIGHT)
    pygame.draw.rect(WIN, BLACK, LEVEL_DISPLAY)

    STARTING_LEVEL_TEXT_WIDTH = 3 * BUFFER
    STARTING_LEVEL_TEXT_HEIGHT = 3 * BUFFER

    STARTING_LEVEL_NUM_WIDTH = 2 * BUFFER + 2 * SQUARE_SIZE
    SCORE_TEXT = "LEVEL"
    for i, char in enumerate(SCORE_TEXT):
        draw_text = TEXT_FONT.render(char, 1, WHITE)
        WIN.blit(draw_text, (STARTING_LEVEL_TEXT_WIDTH +
                 i * SQUARE_SIZE, STARTING_LEVEL_TEXT_HEIGHT))

    level_arr = level % 10, level // 10 % 10
    for i in range(2):
        draw_text = TEXT_FONT.render(str(level_arr[1 - i]), 1, WHITE)
        WIN.blit(draw_text, (STARTING_LEVEL_NUM_WIDTH + i * SQUARE_SIZE,
                 STARTING_LEVEL_TEXT_HEIGHT + SQUARE_SIZE + BUFFER))


def draw_piece(x, y, piece):
    """Draws a piece to the display given the position (x, y) and piece"""

    if len(piece) == 3:
        for i in range(2):
            for j in range(3):
                draw_box(x + SQUARE_SIZE * j, y + SQUARE_SIZE * i, piece[i][j])
    elif len(piece) == 2:
        for i in range(2):
            for j in range(2):
                draw_box(x + BUFFER + SQUARE_SIZE * j,
                         y + SQUARE_SIZE * i, piece[i][j])
    elif len(piece) == 4:
        for j in range(4):
            draw_box(x - BUFFER + SQUARE_SIZE * j, y + BUFFER, piece[1][j])


def draw_next_display(next_pieces):
    """Draws the pieces that are next up"""

    STARTING_NEXT_TEXT_WIDTH = BOARD_WIDTH_PIXLES - \
        (2 * BUFFER + SIDE_DISPLAY_WIDTH_RIGHT) + BUFFER + 1
    STARTING_NEXT_TEXT_HEIGHT = 3 * BUFFER + STATS_DISPLAY_HEIGHT + BUFFER
    STARTING_NEXT_PIECE_WIDTH = STARTING_NEXT_TEXT_WIDTH + BUFFER
    STARTING_NEXT_PIECE_HEIGHT = STARTING_NEXT_TEXT_HEIGHT + SQUARE_SIZE + BUFFER

    NEXT_DISPLAY = pygame.Rect(BOARD_WIDTH_PIXLES - (2 * BUFFER + SIDE_DISPLAY_WIDTH_RIGHT),
                               3 * BUFFER + STATS_DISPLAY_HEIGHT, SIDE_DISPLAY_WIDTH_BOTTEM, NEXT_DISPLAY_HEIGHT)
    pygame.draw.rect(WIN, BLACK, NEXT_DISPLAY)

    NEXT_TEXT = "NEXT"
    for i, char in enumerate(NEXT_TEXT):
        draw_text = TEXT_FONT.render(char, 1, WHITE)
        WIN.blit(draw_text, (STARTING_NEXT_TEXT_WIDTH +
                 i * SQUARE_SIZE, STARTING_NEXT_TEXT_HEIGHT))

    for j in range(4):
        piece = tetris_funct.get_peice(next_pieces[j + 1])
        draw_piece(STARTING_NEXT_PIECE_WIDTH, STARTING_NEXT_PIECE_HEIGHT +
                   j * (SQUARE_SIZE * 2 + BUFFER), piece)


def draw_hold_display(hold_piece):
    """Draws the hold display and updates it with the current held piece if there is one"""

    STARTING_HOLD_TEXT_WIDTH = 3 * BUFFER + SQUARE_SIZE + 1
    STARTING_HOLD_TEXT_HEIGHT = 4 * BUFFER + STATS_DISPLAY_HEIGHT
    STARTING_HOLD_PIECE_WIDTH = STARTING_HOLD_TEXT_WIDTH + BUFFER
    STARTING_HOLD_PIECE_HEIGHT = STARTING_HOLD_TEXT_HEIGHT + SQUARE_SIZE + BUFFER

    HOLD_DISPLAY = pygame.Rect(
        2 * BUFFER + SQUARE_SIZE, 3 * BUFFER + STATS_DISPLAY_HEIGHT, SIDE_DISPLAY_WIDTH_BOTTEM, HOLD_DISPLAY_HEIGHT)
    pygame.draw.rect(WIN, BLACK, HOLD_DISPLAY)

    HOLD_TEXT = "HOLD"
    for i, char in enumerate(HOLD_TEXT):
        draw_text = TEXT_FONT.render(char, 1, WHITE)
        WIN.blit(draw_text, (STARTING_HOLD_TEXT_WIDTH +
                 i * SQUARE_SIZE, STARTING_HOLD_TEXT_HEIGHT))

    if hold_piece != -1:
        piece = tetris_funct.get_peice(hold_piece)
        draw_piece(STARTING_HOLD_PIECE_WIDTH,
                   STARTING_HOLD_PIECE_HEIGHT, piece)
    pygame.display.update()


def display_game_over_screen():
    """Displays the game over screen"""

    draw_text = GAME_OVER_FONT.render("GAME", 1, WHITE)
    draw_text2 = GAME_OVER_FONT.render("OVER", 1, WHITE)
    WIN.blit(draw_text, (BOARD_WIDTH_PIXLES // 2 - (4 * SQUARE_SIZE -
             BUFFER // 2), BOARD_HEIGHT_PIXLES // 2 - (2 * SQUARE_SIZE + BUFFER)))
    WIN.blit(draw_text2, (BOARD_WIDTH_PIXLES // 2 -
             (3 * SQUARE_SIZE - BUFFER // 2), BOARD_HEIGHT_PIXLES // 2 - BUFFER))
    pygame.display.update()


def countdown(d_board):
    """Displays a countdown from 3 to 1"""

    clock = pygame.time.Clock()
    frame = 0
    run = True
    time = 3
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        if frame % (FPS // 2) == 0:
            draw_game_board(d_board)
            draw_text = NUMBER_FONT.render(str(time), 1, WHITE)
            WIN.blit(draw_text, (BOARD_WIDTH_PIXLES // 2 - (draw_text.get_width() //
                     2) - BUFFER, BOARD_HEIGHT_PIXLES // 2 - (draw_text.get_height() // 2)))
            pygame.display.update()
            time -= 1
        frame += 1
        if frame > (FPS // 2) * 3 - 1:
            run = False
    return True


def add_line_cheat(stats):
    """Only to be used in testing. Adds a line to the users stats"""

    stats[1] = stats[1] + 1
    draw_line_display(stats)
    draw_level_display(stats)
    pygame.display.update()


def add_level_cheat(stats):
    """Only to be used in testing. Adds a level to the users stats"""

    stats[1] = stats[1] + 10
    draw_line_display(stats)
    draw_level_display(stats)
    pygame.display.update()


def update_displays(stats, next_pieces):
    """Updates the varity of displays around the game board"""

    draw_next_display(next_pieces)
    draw_line_display(stats)
    draw_score_display(stats)
    draw_level_display(stats)
    pygame.display.update()


def display_pause_screen():
    """Displays the pause screen and varity of buttons the user can interact with"""

    PAUSE_SCREEN_WIDTH = 9 * SQUARE_SIZE
    PAUSE_SCREEN_HEIGHT = 9 * SQUARE_SIZE

    STARTING_PAUSE_WIDTH = 7 * SQUARE_SIZE + 4 * BUFFER
    STARTING_PAUSE_HEIGHT = 7 * SQUARE_SIZE + 6 * BUFFER

    BUTTON_WIDTH = 7 * SQUARE_SIZE
    BUTTON_HEIGHT = SQUARE_SIZE

    STARTING_PAUSED_TEXT_WIDTH = 7 * SQUARE_SIZE + 5 * BUFFER

    PAUSE_SCREEN = pygame.Rect(6 * SQUARE_SIZE + 4 * BUFFER, 4 *
                               SQUARE_SIZE + 6 * BUFFER, PAUSE_SCREEN_WIDTH, PAUSE_SCREEN_HEIGHT)
    pygame.draw.rect(WIN, DARK_GRAY, PAUSE_SCREEN)

    PAUSED_TEXT = "PAUSED"
    for i, char in enumerate(PAUSED_TEXT):
        draw_text = TEXT_FONT.render(char, 1, WHITE)
        WIN.blit(draw_text, (STARTING_PAUSED_TEXT_WIDTH + i *
                 SQUARE_SIZE, 5 * SQUARE_SIZE + 6 * BUFFER))

    RESUME_BUTTON = pygame.Rect(
        STARTING_PAUSE_WIDTH, STARTING_PAUSE_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(WIN, GRAY, RESUME_BUTTON)

    draw_text = PAUSE_FONT.render("RESUME", 1, WHITE)
    WIN.blit(draw_text, (STARTING_PAUSE_WIDTH + (BUTTON_WIDTH // 2) - (draw_text.get_width() //
             2), STARTING_PAUSE_HEIGHT + (BUTTON_HEIGHT // 2) - draw_text.get_height() // 2))

    CONTROLS_BUTTON = pygame.Rect(
        STARTING_PAUSE_WIDTH, STARTING_PAUSE_HEIGHT + SQUARE_SIZE + BUFFER, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(WIN, GRAY, CONTROLS_BUTTON)

    draw_text = PAUSE_FONT.render("CONTROLS", 1, WHITE)
    WIN.blit(draw_text, (STARTING_PAUSE_WIDTH + (BUTTON_WIDTH // 2) - (draw_text.get_width() // 2),
             STARTING_PAUSE_HEIGHT + SQUARE_SIZE + BUFFER + (BUTTON_HEIGHT // 2) - draw_text.get_height() // 2))

    RESTART_BUTTON = pygame.Rect(STARTING_PAUSE_WIDTH, STARTING_PAUSE_HEIGHT +
                                 2 * SQUARE_SIZE + 2 * BUFFER, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(WIN, GRAY, RESTART_BUTTON)

    draw_text = PAUSE_FONT.render("RESTART", 1, WHITE)
    WIN.blit(draw_text, ((BUTTON_WIDTH + 4 * BUFFER) + (BUTTON_WIDTH // 2) - (draw_text.get_width() // 2),
             STARTING_PAUSE_HEIGHT + 2 * SQUARE_SIZE + 2 * BUFFER + (BUTTON_HEIGHT // 2) - draw_text.get_height() // 2))

    QUIT_BUTTON = pygame.Rect(STARTING_PAUSE_WIDTH, STARTING_PAUSE_HEIGHT +
                              3 * SQUARE_SIZE + 3 * BUFFER, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(WIN, GRAY, QUIT_BUTTON)

    draw_text = PAUSE_FONT.render("QUIT", 1, WHITE)
    WIN.blit(draw_text, (STARTING_PAUSE_WIDTH + (BUTTON_WIDTH // 2) - (draw_text.get_width() // 2),
             STARTING_PAUSE_HEIGHT + 3 * SQUARE_SIZE + 3 * BUFFER + (BUTTON_HEIGHT // 2) - draw_text.get_height() // 2))

    pygame.display.update()


def get_button_pressed(x, y):
    """Returns a number based on the position (x, y)"""

    STARTING_PAUSE_WIDTH = 6 * SQUARE_SIZE + 4 * BUFFER
    STARTING_PAUSE_HEIGHT = 4 * SQUARE_SIZE + 6 * BUFFER

    # Returns 0 for resume, 1 for controls, 2 for restart, 3 for quit
    if x > STARTING_PAUSE_WIDTH + SQUARE_SIZE and x < STARTING_PAUSE_WIDTH + 8 * SQUARE_SIZE:
        if y > STARTING_PAUSE_HEIGHT + 3 * SQUARE_SIZE and y < STARTING_PAUSE_HEIGHT + 4 * SQUARE_SIZE:
            return 0
        elif y > STARTING_PAUSE_HEIGHT + 4 * SQUARE_SIZE + BUFFER and y < STARTING_PAUSE_HEIGHT + 5 * SQUARE_SIZE + BUFFER:
            return 1
        elif y > STARTING_PAUSE_HEIGHT + 5 * SQUARE_SIZE + 2 * BUFFER and y < STARTING_PAUSE_HEIGHT + 6 * SQUARE_SIZE + 2 * BUFFER:
            return 2
        elif y > STARTING_PAUSE_HEIGHT + 6 * SQUARE_SIZE + 3 * BUFFER and y < STARTING_PAUSE_HEIGHT + 7 * SQUARE_SIZE + 3 * BUFFER:
            return 3
    return -1


def main():
    clock = pygame.time.Clock()

    run = True
    no_restart = True

    holded_piece = False  # True if user has stored a piece before a new piece as been placed

    hold_piece = -1  # Stores the piece that is displayed in the holded piece display

    time = 0
    loop = 0
    frame = 0
    down = 0
    right = 0
    left = 0

    # Initializes the game board and display board
    game_board = [["*" for i in range(GAME_WIDTH_SQUARES)]
                  for j in range(GAME_HEIGHT_SQUARES)]
    display_board = [["*" for i in range(GAME_WIDTH_SQUARES)]
                     for j in range(GAME_HEIGHT_SQUARES)]

    next_pieces = [random.randint(0, 6) for i in range(5)]

    stats = [0, 0]  # Stores the score and number of ines cleared

    cord = tetris_funct.get_start_cord(next_pieces[0])
    piece = tetris_funct.get_peice(next_pieces[0])

    draw_window()
    draw_game_board(display_board)

    update_displays(stats, next_pieces)
    draw_hold_display(hold_piece)

    if (not countdown(display_board)):
        return False

    tetris_funct.spawn_piece(game_board, display_board, piece, cord)

    draw_game_board(display_board)

    while run:
        clock.tick(FPS)
        loop += 1
        frame += 1

        # Moves the piece down every half a second
        if loop % (FPS // 2) == 0:
            time += 1
            pygame.event.post(pygame.event.Event(MOVE_DOWN))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return False

            if event.type == GAME_OVER:
                run = False

            if event.type == MOVE_DOWN:
                # Determines if there is room to move the piece down
                if (tetris_funct.move_piece_down(game_board, piece, cord)):
                    cord[0] += 1
                    tetris_funct.reset_display_board(game_board, display_board)
                    tetris_funct.place_peice_on_board(
                        display_board, piece, cord)
                    draw_game_board(display_board)
                    loop = 0
                else:
                    tetris_funct.place_peice_on_board(game_board, piece, cord)
                    tetris_funct.clear_lines(game_board, stats)
                    tetris_funct.reset_display_board(game_board, display_board)
                    draw_game_board(display_board)
                    pygame.event.post(pygame.event.Event(NEW_PIECE))
                    holded_piece = False
                    loop = 0

            if event.type == NEW_PIECE and run:
                # Attempts to spawn in a new piece and adds a new piece to the next peice display
                next_pieces.pop(0)
                n = random.randint(0, 6)
                next_pieces.append(n)
                piece = tetris_funct.get_peice(next_pieces[0])
                cord = tetris_funct.get_start_cord(next_pieces[0])

                # Determines if the piece has room to spawn, if not the game ends
                if not tetris_funct.spawn_piece(game_board, display_board, piece, cord):
                    pygame.event.post(pygame.event.Event(GAME_OVER))
                else:
                    update_displays(stats, next_pieces)

                draw_game_board(display_board)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_x:
                    # Rotates the piece clockwise if the user presses Up or X
                    tetris_funct.rotate_clockwise(game_board, piece, cord)
                    tetris_funct.reset_display_board(game_board, display_board)
                    tetris_funct.place_peice_on_board(
                        display_board, piece, cord)
                    draw_game_board(display_board)

                elif event.key == pygame.K_RCTRL or event.key == pygame.K_z:
                    # Rotates the piece counter-clockwise if the user presses Up or X
                    tetris_funct.rotate_counter_clockwise(
                        game_board, piece, cord)
                    tetris_funct.reset_display_board(game_board, display_board)
                    tetris_funct.place_peice_on_board(
                        display_board, piece, cord)
                    draw_game_board(display_board)

                elif (event.key == pygame.K_RSHIFT or event.key == pygame.K_c) and not holded_piece:
                    # Place the current piece into the hold slot if the user presses Right Shift or C
                    if hold_piece == -1:
                        hold_piece = next_pieces[0]
                        tetris_funct.reset_display_board(
                            game_board, display_board)
                        pygame.event.post(pygame.event.Event(NEW_PIECE))
                        loop = 0
                        holded_piece = True
                    else:
                        # Swaps the current piece in holding with the next peice
                        n = hold_piece
                        hold_piece = next_pieces[0]
                        next_pieces[0] = n

                        piece = tetris_funct.get_peice(next_pieces[0])
                        cord = tetris_funct.get_start_cord(next_pieces[0])
                        if not tetris_funct.spawn_piece(game_board, display_board, piece, cord):
                            pygame.event.post(pygame.event.Event(GAME_OVER))
                        tetris_funct.reset_display_board(
                            game_board, display_board)
                        tetris_funct.place_peice_on_board(
                            display_board, piece, cord)
                        draw_game_board(display_board)
                        update_displays(stats, next_pieces)
                        holded_piece = True
                        loop = 0

                    draw_hold_display(hold_piece)

                elif event.key == pygame.K_SPACE:
                    # Drops the piece down as far as possible when the user presses Space
                    stats, cord = tetris_funct.drop_piece(
                        game_board, display_board, piece, stats, cord)
                    draw_game_board(display_board)
                    pygame.event.post(pygame.event.Event(NEW_PIECE))
                    holded_piece = False
                    loop = 0

                elif event.key == pygame.K_ESCAPE:
                    # Displays the menu screen when the user presses Escape
                    display_pause_screen()
                    pause = True
                    while pause:
                        clock.tick(FPS)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                                return False
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    pause = False
                                    if (not countdown(display_board)):
                                        return False
                                    draw_game_board(display_board)

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if pygame.mouse.get_pressed() == (1, 0, 0):

                                    # Determines the button the user pressed
                                    button_pressed = get_button_pressed(
                                        pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

                                    if button_pressed == 0:
                                        # Resume button
                                        pause = False
                                        run = countdown(display_board)
                                        draw_game_board(display_board)
                                    elif button_pressed == 1:
                                        # TODO display control screen
                                        pass
                                    elif button_pressed == 2:
                                        # Restart button
                                        pause = False
                                        no_restart = False
                                        run = False
                                    elif button_pressed == 3:
                                        # Quit button
                                        run = False
                                        return False

                elif event.key == pygame.K_r:
                    # Restarts the game if user presses R
                    no_restart = False
                    run = False

                # Only to be enabled for testing
                #
                # elif event.key == pygame.K_h:
                #     add_line_cheat(stats)
                #
                # elif event.key == pygame.K_j:
                #     add_level_cheat(stats)

        # This code block determines if the user has pressed any of the keys: down, right, or left for over half a second.
        # If they have, it speeds up the action of the block.
        # If they press the key for less than half a second, it performs the action once.
        keys_pressed = pygame.key.get_pressed()
        update = False
        if keys_pressed[pygame.K_DOWN]:
            down += 1
        else:
            down = 0
        if down > FPS / 2:
            if loop > 0.02 * FPS and run:
                pygame.event.post(pygame.event.Event(MOVE_DOWN))
                update = True
        elif down == 1:
            pygame.event.post(pygame.event.Event(MOVE_DOWN))
            update = True

        if keys_pressed[pygame.K_RIGHT]:
            right += 1
        else:
            right = 0
        if right > FPS / 2:
            if frame > 0.05 * FPS:
                tetris_funct.move_piece_right(game_board, piece, cord)
                frame = 0
                update = True
        elif right == 1:
            tetris_funct.move_piece_right(game_board, piece, cord)
            update = True

        if keys_pressed[pygame.K_LEFT]:
            left += 1
        else:
            left = 0
        if left > FPS / 2:
            if frame > 0.02 * FPS:
                tetris_funct.move_piece_left(game_board, piece, cord)
                frame = 0
                update = True
        elif left == 1:
            tetris_funct.move_piece_left(game_board, piece, cord)
            update = True

        if update:
            tetris_funct.reset_display_board(game_board, display_board)
            tetris_funct.place_peice_on_board(display_board, piece, cord)
            draw_game_board(display_board)

    while no_restart:
        # Allows the user to press escape and access the menu after the game has been lost

        display_game_over_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                no_restart = False
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Restarts the game if user presses R
                    no_restart = False

                elif event.key == pygame.K_ESCAPE:
                    # Displays the menu screen when the user presses Escape
                    display_pause_screen()
                    pause = True
                    while pause:
                        clock.tick(FPS)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                no_restart = False
                                return False
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    draw_game_board(display_board)
                                    display_game_over_screen()
                                    pause = False

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if pygame.mouse.get_pressed() == (1, 0, 0):
                                    button_pressed = get_button_pressed(
                                        pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                                    if button_pressed == 0:
                                        # Resume button
                                        pause = False
                                        draw_game_board(display_board)
                                        display_game_over_screen()
                                    elif button_pressed == 1:
                                        # TODO display control screen
                                        pass
                                    elif button_pressed == 2:
                                        # Restart button
                                        pause = False
                                        no_restart = False
                                    elif button_pressed == 3:
                                        # Quit button
                                        pause = False
                                        no_restart == False
                                        return False
    return True


if __name__ == "__main__":
    continue_game = True
    while continue_game:
        continue_game = main()
    print("Thanks for playing :)")
    pygame.quit()
