import pygame
import math

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 30
        self.velocity = 0
        self.gravity = 0.3
        self.jump_strength = -5

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def jump(self):
        self.velocity = self.jump_strength

    def draw(self, screen):
        # Compute wing flap offset (oscillates over time)
        flap_offset = 5 * math.sin(pygame.time.get_ticks() / 100)
        
        # Draw the bird's body as an ellipse
        body_rect = pygame.Rect(
            int(self.x - self.width / 2),
            int(self.y - self.height / 2),
            self.width,
            self.height
        )
        pygame.draw.ellipse(screen, (255, 255, 0), body_rect)  # bright yellow body

        # Draw a dynamic wing using a polygon
        wing_points = [
            (self.x - 5, self.y),
            (self.x - 20, self.y - 10 + flap_offset),
            (self.x - 10, self.y + 5 - flap_offset)
        ]
        pygame.draw.polygon(screen, (238, 221, 130), wing_points)

        # Draw the beak as a small triangle (orange)
        beak_points = [
            (self.x + self.width // 2, self.y - 5),
            (self.x + self.width // 2 + 10, self.y),
            (self.x + self.width // 2, self.y + 5)
        ]
        pygame.draw.polygon(screen, (255, 140, 0), beak_points)

        # Draw the eye as a small black circle
        eye_center = (int(self.x + self.width * 0.15), int(self.y - self.height * 0.2))
        pygame.draw.circle(screen, (0, 0, 0), eye_center, 3)
