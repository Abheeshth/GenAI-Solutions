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