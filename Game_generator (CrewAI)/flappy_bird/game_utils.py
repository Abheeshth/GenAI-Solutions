import pygame

def check_collision(bird, pipe):
    # Create a rectangle around the bird using its width and height.
    bird_rect = pygame.Rect(
        int(bird.x - bird.width / 2),
        int(bird.y - bird.height / 2),
        bird.width,
        bird.height
    )
    
    # Define the top and bottom pipe rectangles.
    top_pipe_rect = pygame.Rect(pipe.x, 0, pipe.width, pipe.gap_y)
    bottom_pipe_rect = pygame.Rect(
        pipe.x, 
        pipe.gap_y + pipe.gap_height, 
        pipe.width, 
        pipe.screen_height - (pipe.gap_y + pipe.gap_height)
    )
    
    if bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect):
        return True
    return False
