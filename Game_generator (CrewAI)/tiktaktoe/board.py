class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.squares = [[None for _ in range(cols)] for _ in range(rows)]

    def mark_square(self, row, col, player):
        self.squares[row][col] = player

    def is_empty(self, row, col):
        return self.squares[row][col] is None

    def get_mark(self, row, col):
        return self.squares[row][col]

    def is_full(self):
        for row in self.squares:
            for mark in row:
                if mark is None:
                    return False
        return True

    def check_win(self, player):
        # Check rows
        for row in self.squares:
            if all(mark == player for mark in row):
                return True
        # Check columns
        for col in range(self.cols):
            if all(self.squares[row][col] == player for row in range(self.rows)):
                return True
        # Check diagonals
        if all(self.squares[i][i] == player for i in range(self.rows)):
            return True
        if all(self.squares[i][self.cols - i - 1] == player for i in range(self.rows)):
            return True
        return False

    def reset(self):
        self.squares = [[None for _ in range(self.cols)] for _ in range(self.rows)]
