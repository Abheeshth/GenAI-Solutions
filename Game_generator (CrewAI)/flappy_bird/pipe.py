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
        # Top pipe with rounded corners
        top_rect = pygame.Rect(self.x, 0, self.width, self.gap_y)
        pygame.draw.rect(screen, (34, 139, 34), top_rect, border_radius=10)  # forest green

        # Bottom pipe with rounded corners
        bottom_rect = pygame.Rect(
            self.x, 
            self.gap_y + self.gap_height, 
            self.width, 
            self.screen_height - (self.gap_y + self.gap_height)
        )
        pygame.draw.rect(screen, (34, 139, 34), bottom_rect, border_radius=10)
