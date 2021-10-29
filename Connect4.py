import numpy as np

rules = '''Connect 4 Rules

OBJECTIVE:

To be the first player to connect 4 of the same colored discs in a row (either vertically, horizontally, or diagonally)
HOW TO PLAY:

First, decide who goes first and what color each player will have. 

Players must alternate turns, and only one disc can be dropped in each turn. 

On your turn, drop one of your colored discs from the top into any of the seven slots. 

The game ends when there is a 4-in-a-row or a stalemate.

The starter of the previous game goes second on the next game.'''
print(rules, "\n")

row_count = int(input("Enter the No of Rows :  "))
col_count = int(input("Enter the No of Columns : "))


def Create_board():
    board = np.zeros((row_count, col_count))
    return board


def drop_piece(board, row, col, piece):
    board[row_count-1][col] = piece


def is_valid_location(board, col):
    return board[5][col] == 0


def get_open_location(board, col):
    for r in range(row_count):
        if board[r][col] == 0:
            return r


def win_move(board, piece):
    # check horizontal  wins
    for c in range(col_count-3):
        for r in range(row_count):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    # check vertical  wins
    for c in range(col_count):
        for r in range(row_count-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    # check +ve diagonal
    for c in range(col_count-3):
        for r in range(row_count-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
  # check -ve diagonal
    for c in range(col_count-3):
        for r in range(3, row_count):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


def print_game(board):
    print(np.flip(board))


def draw_board():
    pass


p1 = input("Enter the Name of Player 1 : ")
p2 = input("Enter the Name of Player 2 : ")
game_over = False
board = Create_board()
print_game(board)
turn = 0

while not game_over:

    # Player 1 Input
    if turn == 0:
        selection = int(input(f"{p1} Enter a choice (0-{row_count}): "))
        if is_valid_location(board, selection):
            row = get_open_location(board, selection)
            drop_piece(board, row, selection, 1)

            if win_move(board, 1):
                print(f"Player {p1} wins !!!!!! Congrulatins")
        print_game(board)

    else:
        selection = int(input(f"{p2} Enter a choice (0-{row_count}): "))
        if is_valid_location(board, selection):
            row = get_open_location(board, selection)
            drop_piece(board, row, selection, 2)
            if win_move(board, 2):
                print(f"Player {p2} wins !!!!!! Congrulatins")

        print_game(board)
    turn += 1
    turn %= 2
