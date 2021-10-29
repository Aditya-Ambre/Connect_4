import numpy as np
import pygame
import sys
import math
from pygame.constants import SYSTEM_CURSOR_ARROW

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
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)


def Create_board():
    board = np.zeros((row_count, col_count))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[row_count-1][col] == 0


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
    print(np.flip(board, 0))


def draw_board(board):
    for c in range(col_count):
        for r in range(row_count):
            pygame.draw.rect(screen, blue, (c*SQUARESIZE, r *
                             SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, black, (int(c*SQUARESIZE+SQUARESIZE/2),
                               int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), radius)

    for c in range(col_count):
        for r in range(row_count):
            if board[r][c] == 1:
                pygame.draw.circle(screen, red, (int(c*SQUARESIZE+SQUARESIZE/2),
                                   height-int(r*SQUARESIZE+SQUARESIZE/2)), radius)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, yellow, (int(
                    c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), radius)
    pygame.display.update()


p1 = input("Enter the Name of Player 1 : ")
p2 = input("Enter the Name of Player 2 : ")
game_over = False
board = Create_board()
print_game(board)
turn = 0

pygame.init()
SQUARESIZE = 100
width = col_count * SQUARESIZE
height = (row_count+1) * SQUARESIZE
size = (width, height)
radius = SQUARESIZE//2 - 5
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
myfont = pygame.font.SysFont("monospace", 60)
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, black, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(
                    screen, red, (posx, int(SQUARESIZE/2)), radius)
            else:
                pygame.draw.circle(
                    screen, yellow, (posx, int(SQUARESIZE/2)), radius)
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, black, (0, 0, width, SQUARESIZE))

            if turn == 0:
                posx = event.pos[0]
                selection = int(math.floor(posx/SQUARESIZE))
            # Player 1 Input
                if is_valid_location(board, selection):
                    row = get_open_location(board, selection)
                    drop_piece(board, row, selection, 1)

                    if win_move(board, 1):
                        label = myfont.render(f"Player {p1} wins!!", 1, red)
                        screen.blit(label, (40, 10))
                        game_over = True

            else:
                # Player 2 Input
                posx = event.pos[0]
                selection = int(math.floor(posx/SQUARESIZE))
                if is_valid_location(board, selection):
                    row = get_open_location(board, selection)
                    drop_piece(board, row, selection, 2)
                    if win_move(board, 2):
                        label = myfont.render(f"Player {p2} wins!!", 1, yellow)
                        screen.blit(label, (40, 10))
                        game_over = True

            print_game(board)
            draw_board(board)
            turn += 1
            turn %= 2
            if game_over:
                pygame.time.wait(3000)
