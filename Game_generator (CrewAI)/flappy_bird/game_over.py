import pygame

def show_game_over(screen, score):
    font_large = pygame.font.SysFont(None, 64)
    font_small = pygame.font.SysFont(None, 48)
    game_over_surface = font_large.render("Game Over", True, (255, 0, 0))
    score_surface = font_small.render(f"Score: {score}", True, (255, 255, 255))
    
    screen_rect = screen.get_rect()
    game_over_rect = game_over_surface.get_rect(center=(screen_rect.centerx, screen_rect.centery - 40))
    score_rect = score_surface.get_rect(center=(screen_rect.centerx, screen_rect.centery + 20))
    
    # Create a semi-transparent overlay for a stylish game over effect
    overlay = pygame.Surface((screen_rect.width, screen_rect.height))
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    
    screen.blit(overlay, (0, 0))
    screen.blit(game_over_surface, game_over_rect)
    screen.blit(score_surface, score_rect)
    pygame.display.flip()
