class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def neighbors_4(self):
        """Returns the four neighboring positions (up, down, left, right)."""
        return [
            Position(self.row - 1, self.col), # Up
            Position(self.row + 1, self.col), # Down
            Position(self.row, self.col - 1), # Left
            Position(self.row, self.col + 1)  # Right
        ]

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.row == other.row and self.col == other.col
        return False

    def __hash__(self):
        return hash((self.row, self.col))

    def __repr__(self):
        return f"({self.row},{self.col})"
