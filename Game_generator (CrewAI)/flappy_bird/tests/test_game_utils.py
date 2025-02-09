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