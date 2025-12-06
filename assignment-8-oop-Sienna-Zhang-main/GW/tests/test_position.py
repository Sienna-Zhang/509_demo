import unittest
import sys
import os

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from GW.position import Position

class TestPosition(unittest.TestCase):
    def test_init(self):
        p = Position(1, 2)
        self.assertEqual(p.row, 1)
        self.assertEqual(p.col, 2)

    def test_eq(self):
        p1 = Position(1, 2)
        p2 = Position(1, 2)
        p3 = Position(2, 1)
        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)
        self.assertNotEqual(p1, "not a position")

    def test_hash(self):
        p1 = Position(1, 2)
        p2 = Position(1, 2)
        s = {p1}
        self.assertIn(p2, s)

    def test_repr(self):
        p = Position(1, 2)
        self.assertEqual(repr(p), "(1,2)")

    def test_neighbors_4(self):
        p = Position(1, 1)
        neighbors = p.neighbors_4()
        expected = [
            Position(0, 1), # Up
            Position(2, 1), # Down
            Position(1, 0), # Left
            Position(1, 2)  # Right
        ]
        # Order might matter depending on implementation, but Position neighbors_4 returns a list in specific order
        self.assertEqual(neighbors, expected)

if __name__ == '__main__':
    unittest.main()
