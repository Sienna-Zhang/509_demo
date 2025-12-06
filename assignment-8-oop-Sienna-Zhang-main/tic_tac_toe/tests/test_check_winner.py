import unittest
import sys
import os

# Add the parent directory to sys.path to import models
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.board import Board

class TestCheckWinner(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_no_winner_empty_board(self):
        self.assertEqual(self.board.check_winner(), "")

    def test_row_winner_x(self):
        self.board.grid = [
            ["X", "X", "X"],
            [" ", "O", " "],
            ["O", " ", " "]
        ]
        self.assertEqual(self.board.check_winner(), "X")

    def test_row_winner_o(self):
        self.board.grid = [
            ["X", " ", "X"],
            ["O", "O", "O"],
            [" ", "X", " "]
        ]
        self.assertEqual(self.board.check_winner(), "O")

    def test_col_winner_x(self):
        self.board.grid = [
            ["X", "O", " "],
            ["X", " ", " "],
            ["X", "O", " "]
        ]
        self.assertEqual(self.board.check_winner(), "X")

    def test_col_winner_o(self):
        self.board.grid = [
            ["X", "O", " "],
            [" ", "O", "X"],
            ["X", "O", " "]
        ]
        self.assertEqual(self.board.check_winner(), "O")

    def test_diagonal_winner_x(self):
        self.board.grid = [
            ["X", "O", " "],
            [" ", "X", "O"],
            [" ", " ", "X"]
        ]
        self.assertEqual(self.board.check_winner(), "X")

    def test_diagonal_winner_o(self):
        self.board.grid = [
            ["X", "X", "O"],
            [" ", "O", " "],
            ["O", " ", "X"]
        ]
        self.assertEqual(self.board.check_winner(), "O")

    def test_draw(self):
        self.board.grid = [
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", "X"]
        ]
        self.assertEqual(self.board.check_winner(), "")

if __name__ == '__main__':
    unittest.main()
