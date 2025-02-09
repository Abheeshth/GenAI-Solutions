Path: flappy_bird/README.md
Code:
'''
# Flappy Bird Game

This is a simple Flappy Bird game developed in Python using Pygame. 

## How to Play
- Press the spacebar to make the bird fly up.
- The bird will fall due to gravity when you are not pressing space.
- Avoid colliding with pipes or the top/bottom walls.
- You gain 1 point for every 2 seconds of survival.

## Folder Structure
- **flappy_bird/main.py**: Main game loop and logic.
- **flappy_bird/bird.py**: Contains the Bird class that handles bird movement.
- **flappy_bird/pipe.py**: Contains the Pipe class that creates obstacles.
- **flappy_bird/game_over.py**: Contains the function to handle game over events.
- **flappy_bird/game_utils.py**: Utility functions (like collision detection).
- **flappy_bird/requirements.txt**: List of dependencies.
- **flappy_bird/assets/**: Folder reserved for game assets.
- **flappy_bird/tests/**: Contains test modules.

## Running the Game
1. Install the requirements: `pip install -r requirements.txt`
2. Run the game: `python main.py`
'''

Path: flappy_bird/requirements.txt
Code:
'''
pygame>=2.0.0
'''

Path: flappy_bird/main.py
Code:
'''
import pygame
import sys
import random
from bird import Bird
from pipe import Pipe
from game_utils import check_collision
from game_over import show_game_over

# Game constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60
PIPE_GAP = 150
PIPE_WIDTH = 70
PIPE_VELOCITY = 3

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Bird")
    clock = pygame.time.Clock()

    # Create bird instance
    bird = Bird(50, SCREEN_HEIGHT // 2)

    # List to store pipes
    pipes = []
    SPAWN_PIPE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_PIPE_EVENT, 1500)  # spawn a new pipe every 1.5 seconds

    # Score variables
    score = 0
    score_timer = 0
    score_interval = 2000  # milliseconds (every 2 secs score increases by 1)

    font = pygame.font.SysFont(None, 36)

    running = True
    while running:
        dt = clock.tick(FPS)
        score_timer += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
            if event.type == SPAWN_PIPE_EVENT:
                # Randomize the gap's vertical position
                gap_y = random.randint(50, SCREEN_HEIGHT - 50 - PIPE_GAP)
                new_pipe = Pipe(SCREEN_WIDTH, gap_y, PIPE_WIDTH, PIPE_GAP, SCREEN_HEIGHT)
                pipes.append(new_pipe)

        # Update bird physics
        bird.update()

        # Update pipe positions
        for pipe in pipes:
            pipe.update(PIPE_VELOCITY)

        # Filter out pipes that have moved off-screen
        pipes = [pipe for pipe in pipes if pipe.x + pipe.width > 0]

        # Check collision with pipes
        for pipe in pipes:
            if check_collision(bird, pipe):
                show_game_over(screen, score)
                pygame.time.delay(2000)
                main()  # Restart game
                return

        # Check collision with floor and ceiling
        if bird.y < 0 or bird.y > SCREEN_HEIGHT:
            show_game_over(screen, score)
            pygame.time.delay(2000)
            main()  # Restart game
            return

        # Update score every 2 seconds
        if score_timer >= score_interval:
            score += 1
            score_timer = 0

        # Drawing routines
        screen.fill((135, 206, 235))  # Sky blue background

        for pipe in pipes:
            pipe.draw(screen)

        bird.draw(screen)

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

if __name__ == "__main__":
    main()
'''

Path: flappy_bird/game_over.py
Code:
'''
import pygame

def show_game_over(screen, score):
    font = pygame.font.SysFont(None, 48)
    game_over_surface = font.render("Game Over", True, (255, 0, 0))
    score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    
    screen_rect = screen.get_rect()
    game_over_rect = game_over_surface.get_rect(center=(screen_rect.centerx, screen_rect.centery - 30))
    score_rect = score_surface.get_rect(center=(screen_rect.centerx, screen_rect.centery + 30))
    
    screen.blit(game_over_surface, game_over_rect)
    screen.blit(score_surface, score_rect)
    pygame.display.flip()
'''

Path: flappy_bird/pipe.py
Code:
'''
import pygame

class Pipe:
    def __init__(self, x, gap_y, width, gap_height, screen_height):
        self.x = x
        self.width = width
        self.gap_y = gap_y
        self.gap_height = gap_height
        self.screen_height = screen_height

    def update(self, velocity):
        self.x -= velocity

    def draw(self, screen):
        # Top pipe rectangle
        top_rect = pygame.Rect(self.x, 0, self.width, self.gap_y)
        # Bottom pipe rectangle
        bottom_rect = pygame.Rect(self.x, self.gap_y + self.gap_height, self.width, self.screen_height - (self.gap_y + self.gap_height))
        
        pygame.draw.rect(screen, (0, 255, 0), top_rect)
        pygame.draw.rect(screen, (0, 255, 0), bottom_rect)
'''

Path: flappy_bird/bird.py
Code:
'''
import pygame

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -10

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def jump(self):
        self.velocity = self.jump_strength

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (int(self.x), int(self.y)), self.radius)
'''

Path: flappy_bird/game_utils.py
Code:
'''
import pygame

def check_collision(bird, pipe):
    # Create a rectangle around the bird (for simple collision detection)
    bird_rect = pygame.Rect(bird.x - bird.radius, bird.y - bird.radius, bird.radius * 2, bird.radius * 2)
    
    # Define top and bottom pipe rectangles
    top_pipe_rect = pygame.Rect(pipe.x, 0, pipe.width, pipe.gap_y)
    bottom_pipe_rect = pygame.Rect(pipe.x, pipe.gap_y + pipe.gap_height, pipe.width, pipe.screen_height - (pipe.gap_y + pipe.gap_height))
    
    if bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect):
        return True
    return False
'''

Path: flappy_bird/assets/.gitkeep
Code:
'''
# This file is intentionally left blank to ensure the assets folder is tracked by version control.
'''

Path: flappy_bird/tests/test_game_utils.py
Code:
'''
import pygame
import unittest
from bird import Bird
from pipe import Pipe
from game_utils import check_collision

class TestGameUtils(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen_height = 600

    def tearDown(self):
        pygame.quit()

    def test_no_collision(self):
        bird = Bird(50, 300)
        pipe = Pipe(300, 200, 70, 150, self.screen_height)
        self.assertFalse(check_collision(bird, pipe))

    def test_collision_with_top_pipe(self):
        bird = Bird(300, 100)
        # Position the pipe so that the top rectangle collides with the bird
        pipe = Pipe(280, 150, 70, 150, self.screen_height)
        self.assertTrue(check_collision(bird, pipe))

    def test_collision_with_bottom_pipe(self):
        bird = Bird(300, 500)
        # Position the pipe so that the bottom rectangle collides with the bird
        pipe = Pipe(280, 300, 70, 150, self.screen_height)
        self.assertTrue(check_collision(bird, pipe))

if __name__ == '__main__':
    unittest.main()
'''