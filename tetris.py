import random
import time
import os

# Constants
WIDTH, HEIGHT = 10, 20
EMPTY, BLOCK = '.', '#'

# Tetromino shapes and their rotations
SHAPES = [
    [['.#..',
      '.#..',
      '.#..',
      '.#..'],
     ['.####']],

    [['..#.',
      '###.',
      '....'],
     ['#..', '###', '..#']],

    [['.#.',
      '###',
      '....'],
     ['##.', '#.#']],

    [['#..',
      '##.',
      '.#.'],
     ['.#.', '###', '..#']],

    [['.##',
      '##.',
      '...'],
     ['.#', '##', '#.']],

    [['##.',
      '.##',
      '...'],
     ['.#', '##', '.#']],

    [['###',
      '...',
      '...'],
     ['###']]
]

# Function to initialize the game board
def create_board():
    return [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Function to display the game board
def display_board(board):
    os.system('clear')
    for row in board:
        print(' '.join(row))
    print('-' * (WIDTH * 2 + 1))

# Function to check if a piece can be placed on the board
def is_valid_position(board, shape, x, y, rotation):
    piece = SHAPES[shape][rotation]
    for row in range(len(piece)):
        for col in range(len(piece[0])):
            if piece[row][col] == '#' and (x + col < 0 or x + col >= WIDTH or y + row >= HEIGHT or board[y + row][x + col] == BLOCK):
                return False
    return True

# Function to clear completed lines
def clear_lines(board):
    full_lines = [i for i, row in enumerate(board) if all(cell == BLOCK for cell in row)]
    for line in full_lines:
        del board[line]
        board.insert(0, [EMPTY] * WIDTH)

# Function to move a piece left
def move_left(board, shape, x, y, rotation):
    if is_valid_position(board, shape, x - 1, y, rotation):
        return x - 1
    return x

# Function to move a piece right
def move_right(board, shape, x, y, rotation):
    if is_valid_position(board, shape, x + 1, y, rotation):
        return x + 1
    return x

# Function to move a piece down
def move_down(board, shape, x, y, rotation):
    if is_valid_position(board, shape, x, y + 1, rotation):
        return y + 1, False
    return y, True

# Main game loop
def tetris_game():
    board = create_board()
    current_shape = random.randint(0, len(SHAPES) - 1)
    x, y, rotation = WIDTH // 2, 0, 0
    game_over = False

    while not game_over:
        display_board(board)

        # Get user input
        user_input = input('Press A to move left, D to move right, S to move down, and Q to quit: ').lower()

        if user_input == 'q':
            game_over = True
            continue

        if user_input == 'a':
            x = move_left(board, current_shape, x, y, rotation)
        elif user_input == 'd':
            x = move_right(board, current_shape, x, y, rotation)
        elif user_input == 's':
            y, game_over = move_down(board, current_shape, x, y, rotation)

        # Update the board with the current piece
        piece = SHAPES[current_shape][rotation]
        for row in range(len(piece)):
            for col in range(len(piece[0])):
                if piece[row][col] == '#':
                    board[y + row][x + col] = BLOCK

        # Check for completed lines and clear them
        clear_lines(board)

        # Generate a new piece if the current piece cannot move down
        if game_over:
            current_shape = random.randint(0, len(SHAPES) - 1)
            x, y, rotation = WIDTH // 2, 0, 0
            game_over = False

# Run the game
tetris_game()

