import pygame
import sys
import random
from board import Board

# Define colors
WHITE   = (255, 255, 255)
BLACK   = (0, 0, 0)
GRAY    = (200, 200, 200)
RED     = (255, 0, 0)
BLUE    = (0, 0, 255)
PURPLE  = (128, 0, 128)
GOLD    = (255, 215, 0)

# Game configuration
WIDTH       = 600
HEIGHT      = 600
LINE_WIDTH  = 10
BOARD_ROWS  = 3
BOARD_COLS  = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS   = SQUARE_SIZE // 3
CIRCLE_WIDTH    = 10
CROSS_WIDTH     = 15
SPACE           = SQUARE_SIZE // 5

# Confetti particle for fancy game-over effects.
class Confetti:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.size = random.randint(4, 8)
        self.speed = random.uniform(1, 3)
        self.color = random.choice([RED, BLUE, GOLD, PURPLE])
    
    def update(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-HEIGHT, 0)
            self.x = random.randint(0, WIDTH)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

class TicTacToeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Fancy TicTacToe")
        self.clock = pygame.time.Clock()
        self.board = Board(BOARD_ROWS, BOARD_COLS)
        self.current_player = "X"  # "X" starts
        self.game_over = False
        self.font_large = pygame.font.SysFont("comicsansms", 72)
        self.font_small = pygame.font.SysFont("comicsansms", 36)
        self.confetti = []
        self.confetti_active = False

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw_window()
            pygame.display.update()
            self.clock.tick(30)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                mouseX, mouseY = event.pos
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE
                if self.board.is_empty(clicked_row, clicked_col):
                    self.board.mark_square(clicked_row, clicked_col, self.current_player)
                    if self.board.check_win(self.current_player):
                        self.game_over = True
                        self.confetti_active = True
                        self.create_confetti()
                    elif self.board.is_full():
                        self.game_over = True
                        self.current_player = None  # Draw
                        self.confetti_active = True
                        self.create_confetti()
                    else:
                        self.switch_player()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.restart_game()

    def update(self):
        if self.confetti_active:
            for conf in self.confetti:
                conf.update()

    def draw_window(self):
        self.draw_background()
        self.draw_lines()
        self.draw_marks()
        if self.game_over:
            self.draw_game_over()

    def draw_background(self):
        # Draw a vertical gradient background (from a light tone to a deeper tone)
        for y in range(HEIGHT):
            # Interpolate between two colors (light blue to a darker blue)
            r = 135 - int((135 - 25) * (y / HEIGHT))
            g = 206 - int((206 - 25) * (y / HEIGHT))
            b = 235 - int((235 - 112) * (y / HEIGHT))
            pygame.draw.line(self.screen, (r, g, b), (0, y), (WIDTH, y))
        # Draw confetti if active
        if self.confetti_active:
            for conf in self.confetti:
                conf.draw(self.screen)

    def draw_lines(self):
        # Draw horizontal and vertical board lines with refined thickness
        for i in range(1, BOARD_ROWS):
            pygame.draw.line(self.screen, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        for i in range(1, BOARD_COLS):
            pygame.draw.line(self.screen, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

    def draw_marks(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                mark = self.board.get_mark(row, col)
                if mark == "O":
                    self.draw_circle(row, col)
                elif mark == "X":
                    self.draw_cross(row, col)

    def draw_circle(self, row, col):
        center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
        # Draw a subtle shadow
        pygame.draw.circle(self.screen, (0, 0, 0), (center[0] + 3, center[1] + 3), CIRCLE_RADIUS)
        pygame.draw.circle(self.screen, BLUE, center, CIRCLE_RADIUS, CIRCLE_WIDTH)

    def draw_cross(self, row, col):
        start_desc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
        end_desc   = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
        start_asc  = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
        end_asc    = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
        shadow_offset = 3
        # Draw shadow for cross
        pygame.draw.line(self.screen, (0, 0, 0),
                         (start_desc[0] + shadow_offset, start_desc[1] + shadow_offset),
                         (end_desc[0] + shadow_offset, end_desc[1] + shadow_offset), CROSS_WIDTH)
        pygame.draw.line(self.screen, (0, 0, 0),
                         (start_asc[0] + shadow_offset, start_asc[1] + shadow_offset),
                         (end_asc[0] + shadow_offset, end_asc[1] + shadow_offset), CROSS_WIDTH)
        pygame.draw.line(self.screen, RED, start_desc, end_desc, CROSS_WIDTH)
        pygame.draw.line(self.screen, RED, start_asc, end_asc, CROSS_WIDTH)

    def draw_game_over(self):
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        if self.current_player is None:
            text = self.font_large.render("Draw!", True, WHITE)
        else:
            text = self.font_large.render(f"{self.current_player} Wins!", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(text, text_rect)
        restart_text = self.font_small.render("Press R to Restart", True, WHITE)
        restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80))
        self.screen.blit(restart_text, restart_rect)

    def create_confetti(self):
        self.confetti = [Confetti() for _ in range(100)]

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def restart_game(self):
        self.board.reset()
        self.current_player = "X"
        self.game_over = False
        self.confetti_active = False
