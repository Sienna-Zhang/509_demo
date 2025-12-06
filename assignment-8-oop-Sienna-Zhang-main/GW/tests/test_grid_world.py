import unittest
import sys
import os

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from GW.position import Position
from GW.grid_world import GridWorld

class TestGridWorld(unittest.TestCase):
    def setUp(self):
        self.world = GridWorld(5, 5)

    def test_init(self):
        self.assertEqual(self.world.rows, 5)
        self.assertEqual(self.world.cols, 5)
        self.assertEqual(self.world.start, Position(0, 0))
        self.assertEqual(self.world.goal, Position(4, 4))

    def test_in_bounds(self):
        self.assertTrue(self.world.in_bounds(Position(0, 0)))
        self.assertTrue(self.world.in_bounds(Position(4, 4)))
        self.assertFalse(self.world.in_bounds(Position(-1, 0)))
        self.assertFalse(self.world.in_bounds(Position(0, 5)))

    def test_passable(self):
        p = Position(1, 1)
        self.assertTrue(self.world.passable(p))
        self.world.place_wall(p)
        self.assertFalse(self.world.passable(p))

    def test_place_remove_wall(self):
        p = Position(1, 1)
        self.world.place_wall(p)
        self.assertIn(p, self.world.walls)
        self.world.remove_wall(p)
        self.assertNotIn(p, self.world.walls)

    def test_cannot_place_wall_on_start_or_goal(self):
        self.world.place_wall(self.world.start)
        self.assertNotIn(self.world.start, self.world.walls)
        self.world.place_wall(self.world.goal)
        self.assertNotIn(self.world.goal, self.world.walls)

    def test_is_goal(self):
        self.assertTrue(self.world.is_goal(self.world.goal))
        self.assertFalse(self.world.is_goal(self.world.start))

if __name__ == '__main__':
    unittest.main()
