Path: ticktacktoe/game.py
Code:
'''
from ticktacktoe.utils import check_winner

class Game:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None

    def make_move(self, row, col):
        if self.board[row][col] == '' and not self.game_over:
            self.board[row][col] = self.current_player
            self.winner = check_winner(self.board)
            if self.winner or self.is_draw():
                self.game_over = True
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def is_draw(self):
        for row in self.board:
            if '' in row:
                return False
        return True

    def reset(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None

if __name__ == "__main__":
    # For direct execution, start the UI
    from ticktacktoe.ui import run_game
    run_game()
'''
  
Path: ticktacktoe/ui.py
Code:
'''
import sys
import pygame
from ticktacktoe.game import Game

# Constants and configurations
WIDTH, HEIGHT = 300, 300
LINE_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
X_COLOR = (200, 0, 0)
O_COLOR = (0, 0, 200)
LINE_WIDTH = 5
BOARD_ROWS = 3
BOARD_COLS = 3

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

def draw_board(game):
    screen.fill(BG_COLOR)
    cell_size = WIDTH // 3
    # Draw grid lines
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (i * cell_size, 0), (i * cell_size, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, i * cell_size), (WIDTH, i * cell_size), LINE_WIDTH)
    
    # Draw marks
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if game.board[row][col] == 'X':
                draw_x(row, col, cell_size)
            elif game.board[row][col] == 'O':
                draw_o(row, col, cell_size)
    pygame.display.update()

def draw_x(row, col, cell_size):
    offset = cell_size // 4
    start_pos = (col * cell_size + offset, row * cell_size + offset)
    end_pos = ((col + 1) * cell_size - offset, (row + 1) * cell_size - offset)
    pygame.draw.line(screen, X_COLOR, start_pos, end_pos, LINE_WIDTH)
    start_pos = (col * cell_size + offset, (row + 1) * cell_size - offset)
    end_pos = ((col + 1) * cell_size - offset, row * cell_size + offset)
    pygame.draw.line(screen, X_COLOR, start_pos, end_pos, LINE_WIDTH)

def draw_o(row, col, cell_size):
    center = (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2)
    radius = cell_size // 3
    pygame.draw.circle(screen, O_COLOR, center, radius, LINE_WIDTH)

def display_winner(game):
    font = pygame.font.SysFont(None, 40)
    if game.winner:
        text = font.render(f"Winner: {game.winner}", True, (0, 150, 0))
    elif game.is_draw():
        text = font.render("Draw!", True, (0, 150, 0))
    else:
        return
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.update()

def run_game():
    game = Game()
    clock = pygame.time.Clock()
    cell_size = WIDTH // 3
    running = True
    while running:
        draw_board(game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not game.game_over:
                    mouseX, mouseY = event.pos
                    row = mouseY // cell_size
                    col = mouseX // cell_size
                    game.make_move(row, col)
                else:
                    game.reset()
        if game.game_over:
            display_winner(game)
        clock.tick(30)
'''
  
Path: ticktacktoe/utils.py
Code:
'''
def check_winner(board):
    # Check rows
    for row in board:
        if row[0] != '' and row[0] == row[1] == row[2]:
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] != '' and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    # Check diagonals
    if board[0][0] != '' and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != '' and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None
'''
  
Path: ticktacktoe/requirements.txt
Code:
'''
pygame
'''
  
Path: ticktacktoe/README.md
Code:
'''
Tic Tac Toe Game
================

A simple Tic Tac Toe game implemented in Python with pygame.

How to Run:
-----------
1. Install dependencies:
   pip install -r ticktacktoe/requirements.txt

2. Run the game:
   python -m ticktacktoe.game

Gameplay:
-----------
- Click on a cell to place your mark (X or O).
- The game alternates moves between X and O.
- After a win or draw, click to reset the game.
'''
  
Path: ticktacktoe/LICENSE
Code:
'''
MIT License

Copyright (c) 2023

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
'''
  
Path: tests/test_game.py
Code:
'''
import unittest
from ticktacktoe.game import Game
from ticktacktoe.utils import check_winner

class TestGameLogic(unittest.TestCase):
    def test_win_row(self):
        game = Game()
        game.board = [
            ['X', 'X', 'X'],
            ['', 'O', ''],
            ['', '', 'O']
        ]
        self.assertEqual(check_winner(game.board), 'X')

    def test_win_column(self):
        game = Game()
        game.board = [
            ['O', 'X', ''],
            ['O', 'X', ''],
            ['O', '', 'X']
        ]
        self.assertEqual(check_winner(game.board), 'O')

    def test_win_diagonal(self):
        game = Game()
        game.board = [
            ['X', 'O', ''],
            ['', 'X', 'O'],
            ['', '', 'X']
        ]
        self.assertEqual(check_winner(game.board), 'X')

    def test_draw(self):
        game = Game()
        game.board = [
            ['X', 'O', 'X'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X']
        ]
        self.assertIsNone(check_winner(game.board))
        self.assertTrue(game.is_draw())

if __name__ == '__main__':
    unittest.main()
'''
  
Path: tests/test_ui.py
Code:
'''
import unittest
import pygame
from ticktacktoe.ui import draw_board

class TestUI(unittest.TestCase):
    def test_draw_board(self):
        # Create a dummy game object with an empty board
        class DummyGame:
            board = [['' for _ in range(3)] for _ in range(3)]
        dummy = DummyGame()
        try:
            draw_board(dummy)
            result = True
        except Exception:
            result = False
        self.assertTrue(result)

if __name__ == '__main__':
    pygame.display.init()
    unittest.main()
'''
  
Path: docs/development_guide.md
Code:
'''
# Development Guide for Tic Tac Toe Game

## Overview
This project implements a simple Tic Tac Toe game using Python and pygame.

## Directory Structure
- ticktacktoe/
  - game.py: Contains the main game logic.
  - ui.py: Manages the game's user interface.
  - utils.py: Utility functions for game operations.
  - requirements.txt: Lists the project dependencies.
  - README.md: Overview and instructions.
  - LICENSE: Licensing information.
- tests/
  - test_game.py: Unit tests for game logic.
  - test_ui.py: Unit tests for the UI components.
- docs/
  - development_guide.md: This development guide.

## Coding Guidelines
- Use clear and descriptive names for variables and functions.
- Keep game logic, UI, and utilities in separate modules.
- Write unit tests to ensure code reliability.
- Handle user inputs gracefully and reset the game state as needed.

## Running the Game
1. Install dependencies:
   pip install -r ticktacktoe/requirements.txt

2. Run the game:
   python -m ticktacktoe.game

## Best Practices
- Maintain modular and readable code.
- Ensure the game loop runs at a stable frame rate.
- Update the UI responsively to user input.
'''