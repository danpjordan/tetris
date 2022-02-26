import random
import time


def print_array(board):
    """Prints the board to the console"""
    for row in board:
        for col in row:
            print(col, "", end="")
        print()
    print()


def rotate_clockwise(g_board, piece, cord):
    """Rotates a peice clockwise only if there is space for that piece to rotate to"""

    successful_rotate = True

    # Determines which type of piece is being rotated inorder to define the rotate behavior
    if len(piece) == 3:
        # Rotates the peice that will be placed onto the game board
        temp = piece[0][0]
        piece[0][0] = piece[2][0]
        piece[2][0] = piece[2][2]
        piece[2][2] = piece[0][2]
        piece[0][2] = temp
        temp = piece[0][1]
        piece[0][1] = piece[1][0]
        piece[1][0] = piece[2][1]
        piece[2][1] = piece[1][2]
        piece[1][2] = temp

        # Determines if the newly rotated piece will contridict with the existing game board
        # If there is a contridiction, then it undoes the rotation
        if cord[0] + 2 > 19 or cord[1] < 0 or cord[1] + 2 > 9:
            successful_rotate = False
        else:
            for i in range(3):
                for j in range(3):
                    if piece[i][j] != "*" and g_board[cord[0] + i][cord[1] + j] != "*":
                        successful_rotate = False

        # Undoes the roation of the piece if attempted rotated failed
        if not successful_rotate:
            temp = piece[0][0]
            piece[0][0] = piece[0][2]
            piece[0][2] = piece[2][2]
            piece[2][2] = piece[2][0]
            piece[2][0] = temp
            temp = piece[0][1]
            piece[0][1] = piece[1][2]
            piece[1][2] = piece[2][1]
            piece[2][1] = piece[1][0]
            piece[1][0] = temp

    elif len(piece) == 4:
        # Rotates the peice that will be placed onto the game board
        temp = piece[0][1]
        piece[0][1] = piece[2][0]
        piece[2][0] = piece[3][2]
        piece[3][2] = piece[1][3]
        piece[1][3] = temp
        temp = piece[0][2]
        piece[0][2] = piece[1][0]
        piece[1][0] = piece[3][1]
        piece[3][1] = piece[2][3]
        piece[2][3] = temp
        temp = piece[1][1]
        piece[1][1] = piece[2][1]
        piece[2][1] = piece[2][2]
        piece[2][2] = piece[1][2]
        piece[1][2] = temp

        # Determines if the nelyw rotated piece will contridict with the existing game board
        # If there is a contridiction, then it undoes the rotation
        if cord[0] < 0 or cord[0] + 3 > 19 or cord[1] < 0 or cord[1] + 3 > 9:
            successful_rotate = False
        else:
            for i in range(4):
                for j in range(4):
                    if piece[i][j] != "*" and g_board[cord[0] + i][cord[1] + j] != "*":
                        successful_rotate = False

        # Undoes the roation of the piece if attempted rotated failed
        if not successful_rotate:
            temp = piece[0][1]
            piece[0][1] = piece[1][3]
            piece[1][3] = piece[3][2]
            piece[3][2] = piece[2][0]
            piece[2][0] = temp
            temp = piece[0][2]
            piece[0][2] = piece[2][3]
            piece[2][3] = piece[3][1]
            piece[3][1] = piece[1][0]
            piece[1][0] = temp
            temp = piece[1][1]
            piece[1][1] = piece[1][2]
            piece[1][2] = piece[2][2]
            piece[2][2] = piece[2][1]
            piece[2][1] = temp


def rotate_counter_clockwise(g_board, piece, cord):
    """Rotates a peice counter-clockwise only if there is space for that piece to rotate to"""

    successful_rotate = True

    # Determines which type of piece is being rotated inorder to define the rotate behavior
    if len(piece) == 3:
        # Rotates the peice that will be placed onto the game board
        temp = piece[0][0]
        piece[0][0] = piece[0][2]
        piece[0][2] = piece[2][2]
        piece[2][2] = piece[2][0]
        piece[2][0] = temp
        temp = piece[0][1]
        piece[0][1] = piece[1][2]
        piece[1][2] = piece[2][1]
        piece[2][1] = piece[1][0]
        piece[1][0] = temp

        # Determines if the newly rotated piece will contridict with the existing game board
        # If there is a contridiction, then it undoes the rotation
        if cord[0] + 2 > 19 or cord[1] < 0 or cord[1] + 2 > 9:
            successful_rotate = False
        else:
            for i in range(3):
                for j in range(3):
                    if piece[i][j] != "*" and g_board[cord[0] + i][cord[1] + j] != "*":
                        successful_rotate = False

        # Undoes the roation of the piece if attempted rotated failed
        if not successful_rotate:
            temp = piece[0][0]
            piece[0][0] = piece[2][0]
            piece[2][0] = piece[2][2]
            piece[2][2] = piece[0][2]
            piece[0][2] = temp
            temp = piece[0][1]
            piece[0][1] = piece[1][0]
            piece[1][0] = piece[2][1]
            piece[2][1] = piece[1][2]
            piece[1][2] = temp

    elif len(piece) == 4:
        # Rotates the peice that will be placed onto the game board
        temp = piece[0][1]
        piece[0][1] = piece[1][3]
        piece[1][3] = piece[3][2]
        piece[3][2] = piece[2][0]
        piece[2][0] = temp
        temp = piece[0][2]
        piece[0][2] = piece[2][3]
        piece[2][3] = piece[3][1]
        piece[3][1] = piece[1][0]
        piece[1][0] = temp
        temp = piece[1][1]
        piece[1][1] = piece[1][2]
        piece[1][2] = piece[2][2]
        piece[2][2] = piece[2][1]
        piece[2][1] = temp

        # Determines if the newly rotated piece will contridict with the existing game board
        # If there is a contridiction, then it undoes the rotation
        if cord[0] < 0 or cord[0] + 3 > 19 or cord[1] < 0 or cord[1] + 3 > 9:
            successful_rotate = False
        else:
            for i in range(4):
                for j in range(4):
                    if piece[i][j] != "*" and g_board[cord[0] + i][cord[1] + j] != "*":
                        successful_rotate = False

        # Undoes the roation of the piece if attempted rotated failed
        if not successful_rotate:
            temp = piece[0][1]
            piece[0][1] = piece[2][0]
            piece[2][0] = piece[3][2]
            piece[3][2] = piece[1][3]
            piece[1][3] = temp
            temp = piece[0][2]
            piece[0][2] = piece[1][0]
            piece[1][0] = piece[3][1]
            piece[3][1] = piece[2][3]
            piece[2][3] = temp
            temp = piece[1][1]
            piece[1][1] = piece[2][1]
            piece[2][1] = piece[2][2]
            piece[2][2] = piece[1][2]
            piece[1][2] = temp


def get_peice(n):
    """Returned the array of a piece"""

    if (n == 0):
        return [["$", "$", "$"],
                ["*", "$", "*"],
                ["*", "*", "*"]]
    elif (n == 1):
        return [["*", "+", "+"],
                ["+", "+", "*"],
                ["*", "*", "*"]]
    elif (n == 2):
        return [["-", "-", "*"],
                ["*", "-", "-"],
                ["*", "*", "*"]]
    elif (n == 3):
        return [["#", "#", "#"],
                ["#", "*", "*"],
                ["*", "*", "*"]]
    elif (n == 4):
        return [["=", "=", "="],
                ["*", "*", "="],
                ["*", "*", "*"]]
    elif (n == 5):
        return [["%", "%"],
                ["%", "%"]]
    elif (n == 6):
        return [["*", "*", "*", "*"],
                ["@", "@", "@", "@"],
                ["*", "*", "*", "*"],
                ["*", "*", "*", "*"]]


def get_start_cord(n):
    """Gets the coordinate of the top left edege of the piece"""

    if n < 5:
        return [0, 3]
    elif n == 5:
        return [0, 4]
    elif n == 6:
        return [-1, 3]


def reset_display_board(g_board, d_board):
    """Maps the borad that is displayed to the user to the game board"""

    for i in range(20):
        for j in range(10):
            d_board[i][j] = g_board[i][j]


def print_boards(g_board, d_board):
    """Prints the two different boards to the console"""
    print("Game board")
    print_array(g_board)
    print("Display board")
    print_array(d_board)


def place_peice_on_board(d_board, piece, cord):
    """Place the piece on the display board at the coordinate given"""

    if len(piece) == 2:
        for i in range(2):
            for j in range(2):
                if piece[i][j] != "*":
                    d_board[cord[0] + i][cord[1] + j] = piece[i][j]
    if len(piece) == 3:
        for i in range(3):
            for j in range(3):
                if piece[i][j] != "*":
                    d_board[cord[0] + i][cord[1] + j] = piece[i][j]
    if len(piece) == 4:
        for i in range(4):
            for j in range(4):
                if piece[i][j] != "*":
                    d_board[cord[0] + i][cord[1] + j] = piece[i][j]


def move_piece_left(g_board, piece, cord):
    """Moves the piece to the left if there is not another piece or the wall in the way"""

    # Determines which type of piece is being move inorder to define the movement behavior
    if len(piece) == 2:
        # Checks to see if piece will collide with the wall
        if cord[1] - 1 < 0:
            return 0

        # Checks the tiles directly to the right of the piece to determine if there is another piece
        for i in range(2):
            j = 0
            if (piece[i][j] != "*" and g_board[cord[0] + i][cord[1] + j - 1] != "*"):
                return 0

    elif len(piece) == 3:
        # Checks to see if piece will collide with the wall
        if cord[1] - 1 < 0:
            for i in range(3):
                if piece[i][0] != "*":
                    return 0
        if cord[1] - 1 < -1:
            for i in range(3):
                if piece[i][1] != "*":
                    return 0

        # Checks the tiles directly to the right of the piece to determine if there is another piece
        for i in range(3):
            for j in range(3):
                if (piece[i][j] != "*" and g_board[cord[0] + i][cord[1] + j - 1] != "*"):
                    return 0

    elif len(piece) == 4:
        # Checks to see if piece will collide with the wall
        if cord[1] - 1 < 0:
            for i in range(4):
                if piece[i][0] != "*":
                    return 0
            if piece[0][1] != "*":
                if cord[1] - 1 < -1:
                    return 0
            if piece[0][2] != "*":
                if cord[1] - 1 < -2:
                    return 0

        # Checks the tiles directly to the right of the piece to determine if there is another piece
        for i in range(4):
            for j in range(4):
                if (piece[i][j] != "*" and g_board[cord[0] + i][cord[1] + j - 1] != "*"):
                    return 0

    # If no collisions have been dectected, the position of the piece is updated
    cord[1] -= 1
    return 1


def move_piece_right(g_board, piece, cord):
    """Moves the piece to the right if there is not another piece or the wall in the way"""

    # Determines which type of piece is being move inorder to define the movement behavior
    if len(piece) == 2:
        # Checks to see if piece will collide with the wall
        if cord[1] + 2 > 9:
            return 0

        # Checks the tiles directly to the right of the piece to determine if there is another piece
        for i in range(2):
            if (piece[i][1] != "*" and g_board[cord[0] + i][cord[1] + 2] != "*"):
                return 0

    elif len(piece) == 3:
        # Checks to see if piece will collide with the wall
        if cord[1] + 3 > 9:
            for i in range(3):
                if piece[i][2] != "*":
                    return 0
        if cord[1] + 3 > 10:
            for i in range(3):
                if piece[i][1] != "*":
                    return 0

        # Checks the tiles directly to the right of the piece to determine if there is another peice
        for i in range(3):
            for j in range(3):
                if (piece[i][j] != "*" and g_board[cord[0] + i][cord[1] + j + 1] != "*"):
                    return 0

    elif len(piece) == 4:
        # Checks to see if piece will collide with the wall
        if cord[1] + 4 > 9:
            for i in range(4):
                if piece[i][3] != "*":
                    return 0
            if piece[0][1] != "*":
                if cord[1] + 1 > 8:
                    return 0
            if piece[0][2] != "*":
                if cord[1] + 1 > 7:
                    return 0

        # Checks the tiles directly to the right of the piece to determine if there is another peice
        for i in range(4):
            for j in range(4):
                if (piece[i][j] != "*" and g_board[cord[0] + i][cord[1] + j + 1] != "*"):
                    return 0

    # If no collisions have been dectected, the position of the piece is updated
    cord[1] += 1
    return 1


def move_piece_down(g_board, piece, cord):
    """Determines if a piece can be moved down"""

    # Determines if the piece will hit the floor based on which type of piece is falling
    if len(piece) == 2 and cord[0] + 2 > 19:
        return False
    elif len(piece) == 3 and cord[0] + 3 > 19:
        if cord[0] + 3 == 20:
            for i in range(3):
                if piece[2][i] != "*":
                    return False
        else:
            return False
    elif len(piece) == 4 and cord[0] + 4 > 19:
        if cord[0] + 4 == 20:
            for i in range(4):
                if piece[3][i] != "*":
                    return False
        elif cord[0] + 4 == 21:
            for i in range(4):
                if piece[2][i] != "*":
                    return False
        elif cord[0] + 4 == 22:
            return False

    # Determines which type of piece is being move inorder to define the movement behavior
    if len(piece) == 2:
        # Determines if the piece will hit another piece
        for j in range(2):
            if g_board[cord[0] + 2][cord[1] + j] != "*":
                return False
    elif len(piece) == 3:
        # Determines if the piece will hit another piece
        for j in range(3):
            for i in range(3):
                if piece[2 - i][j] != "*":
                    if g_board[cord[0] + 2 - i + 1][cord[1] + j] != "*":
                        return False
    elif len(piece) == 4:
        # Determines if the piece will hit another piece
        for j in range(4):
            for i in range(4):
                if piece[3 - i][j] != "*":
                    if g_board[cord[0] + 3 - i + 1][cord[1] + j] != "*":
                        return False

    # If no collisions have been dectected, True is returned
    return True


def spawn_piece(g_board, d_board, piece, cord):
    """Attemps to spawn a new piece at the top of the board"""

    # Determines which type of piece is being move inorder to define the spawning behavior
    if len(piece) == 2:
        # Checks if there is a piece at the position where the piece would spawn
        for i in range(2):
            for j in range(2):
                if g_board[i][cord[1] + j] != "*":
                    return False

    elif len(piece) == 3:
        # Checks if there is a piece at the position where the piece would spawn
        for i in range(3):
            for j in range(3):
                if piece[i][j] != "*" and g_board[cord[0] + i][cord[1] + j] != "*":
                    return False

    elif len(piece) == 4:
        # Checks if there is a piece at the position where the piece would spawn
        for j in range(4):
            if g_board[0][cord[1] + j] != "*":
                return False

    # If there is space for the piece to spawn, the piece is placed on the board
    place_peice_on_board(d_board, piece, cord)
    return True


def clear_line(g_board, line):
    """Clears a line by shifting all rows above the line down one tile"""

    for i in range(line):
        for j in range(10):
            g_board[line - i][j] = g_board[line - i - 1][j]
    for j in range(10):
        g_board[0][j] = "*"


def clear_lines(g_board, stats):
    """Determines which lines, if any, need to be cleared and then clears those lines"""

    # Marks which lines need to be clearend
    lines_to_clear = []
    current_line = -20
    for i in range(20):
        count = 0
        for j in range(10):
            if g_board[19 - i][j] != "*":
                count += 1
            else:
                break
        if count == 10:
            lines_to_clear.append(19 - i)
            current_line = 0
        current_line += 1
        if current_line == 4:
            break

    # Clears the lines that have been marked for clearing
    lines_to_clear.reverse()
    for line in lines_to_clear:
        clear_line(g_board, line)

    # Sets the level to reflect how many lines have been cleared
    level = min(29, 1 + stats[1] // 10)

    # Updates the game stats in accordance with how many lines were cleared
    if len(lines_to_clear) == 1:
        stats[0] += 40 * (level)
    if len(lines_to_clear) == 2:
        stats[0] += 100 * (level)
    if len(lines_to_clear) == 3:
        stats[0] += 300 * (level)
    if len(lines_to_clear) == 4:
        stats[0] += 1200 * (level)
    stats[1] += len(lines_to_clear)


def drop_piece(g_board, d_board, piece, stats, cord):
    """Moves the piece down until it hits the floor or another piece"""

    while(move_piece_down(g_board, piece, cord)):
        # Determines where the piece collides with the floor or another piece
        cord[0] += 1
        reset_display_board(g_board, d_board)
        place_peice_on_board(d_board, piece, cord)
    else:
        # When a collision has been detected
        # The piece is placed on the game board
        place_peice_on_board(g_board, piece, cord)

        # Lines, if any, are cleared and the stats are updated accordingly
        clear_lines(g_board, stats)
        reset_display_board(g_board, d_board)

    return stats, cord


if __name__ == "__main__":
    """This runs tetris in the console. 
    A and D to move left and right, W or Space to spin, S or No-Input to drop faster"""

    game_board = [["*" for i in range(10)] for j in range(20)]
    display_board = [["*" for i in range(10)] for j in range(20)]
    stats = [0, 0]  # score, lines cleared
    cont = True

    while cont:
        n = random.randint(0, 6)
        piece = get_peice(n)
        cord = get_start_cord(n)
        cont = spawn_piece(game_board, display_board, piece, cord)
        print("Score: {}".format(stats[0]))
        print_array(display_board)
        run = True
        while run and cont:
            user_move_input = ""
            move_down = False
            start = time.time()
            while not move_down:
                user_move_input = input("Enter your move: ")
                if user_move_input == " ":
                    rotate_clockwise(game_board, piece, cord)
                elif user_move_input == "w":
                    rotate_counter_clockwise(game_board, piece, cord)
                elif user_move_input == "a":
                    move_piece_left(game_board, piece, cord)
                elif user_move_input == "d":
                    move_piece_right(game_board, piece, cord)
                elif user_move_input == "s":
                    move_down = True
                reset_display_board(game_board, display_board)
                place_peice_on_board(display_board, piece, cord)
                print("Score: {}".format(stats[0]))
                print_array(display_board)
                end = time.time()
                if end - start >= 1 or user_move_input == "":
                    move_down = True
                if user_move_input == "":
                    move_down = True

            if move_piece_down(game_board, piece, cord):
                cord[0] += 1
                reset_display_board(game_board, display_board)
                place_peice_on_board(display_board, piece, cord)
                print("Score: {}".format(stats[0]))
                print_array(display_board)
            else:
                place_peice_on_board(game_board, piece, cord)
                clear_lines(game_board, stats)
                print("Score: {}".format(stats[0]))
                reset_display_board(game_board, display_board)
                print_array(display_board)
                run = False

    print("Game Over.\nYou got to level {} with a score of {} and {} lines cleared!".format(
        stats[1] // 10, stats[0], stats[1]))
