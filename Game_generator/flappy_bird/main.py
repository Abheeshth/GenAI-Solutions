import pygame
import sys
import random
from bird import Bird
from pipe import Pipe
from game_utils import check_collision
from game_over import show_game_over
import math

# Game constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60
PIPE_GAP = 150
PIPE_WIDTH = 70
PIPE_VELOCITY = 3

# Cloud settings
NUM_CLOUDS = 5

class Cloud:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(20, 150)
        self.speed = random.uniform(0.2, 0.8)
        self.size = random.randint(30, 60)
    
    def update(self):
        self.x -= self.speed
        if self.x < -self.size:
            self.x = SCREEN_WIDTH + self.size
            self.y = random.randint(20, 150)
    
    def draw(self, screen):
        # Draw cloud as overlapping circles for a fluffy effect
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.size)
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x + self.size//2), int(self.y + self.size//4)), self.size//2)
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x - self.size//2), int(self.y + self.size//4)), self.size//2)

def draw_background(screen, clouds):
    # Draw a vertical gradient sky (from light blue to deep blue)
    for i in range(SCREEN_HEIGHT):
        r = int(135 + (25 - 135) * (i / SCREEN_HEIGHT))
        g = int(206 + (25 - 206) * (i / SCREEN_HEIGHT))
        b = int(235 + (112 - 235) * (i / SCREEN_HEIGHT))
        pygame.draw.line(screen, (r, g, b), (0, i), (SCREEN_WIDTH, i))
    
    # Draw clouds
    for cloud in clouds:
        cloud.draw(screen)
    
    # Draw a moving ground (simulate scrolling ground)
    ground_height = 50
    pygame.draw.rect(screen, (50, 205, 50), (0, SCREEN_HEIGHT - ground_height, SCREEN_WIDTH, ground_height))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Bird")
    clock = pygame.time.Clock()

    # Create the bird instance
    bird = Bird(50, SCREEN_HEIGHT // 2)

    # List to store pipes
    pipes = []
    SPAWN_PIPE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_PIPE_EVENT, 1500)  # spawn a new pipe every 1.5 seconds

    # Create clouds
    clouds = [Cloud() for _ in range(NUM_CLOUDS)]

    # Score variables
    score = 0
    score_timer = 0
    score_interval = 2000  # every 2 seconds, score increases by 1

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

        # Update background clouds
        for cloud in clouds:
            cloud.update()

        # Update bird physics
        bird.update()

        # Update pipe positions
        for pipe in pipes:
            pipe.update(PIPE_VELOCITY)

        # Remove pipes that have moved off-screen
        pipes = [pipe for pipe in pipes if pipe.x + pipe.width > 0]

        # Check collisions with pipes
        for pipe in pipes:
            if check_collision(bird, pipe):
                show_game_over(screen, score)
                pygame.time.delay(2000)
                main()  # Restart game
                return

        # Check collision with floor and ceiling (accounting for ground height)
        if bird.y < 0 or bird.y > SCREEN_HEIGHT - 50:
            show_game_over(screen, score)
            pygame.time.delay(2000)
            main()  # Restart game
            return

        # Update score every 2 seconds
        if score_timer >= score_interval:
            score += 1
            score_timer = 0

        # Draw the background (gradient sky, clouds, and ground)
        draw_background(screen, clouds)

        # Draw pipes
        for pipe in pipes:
            pipe.draw(screen)

        # Draw the bird
        bird.draw(screen)

        # Draw the score
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

if __name__ == "__main__":
    main()
