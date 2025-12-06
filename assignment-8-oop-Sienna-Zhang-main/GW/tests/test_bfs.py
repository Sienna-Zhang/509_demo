import unittest
import sys
import os

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from GW.position import Position
from GW.grid_world import GridWorld
from GW.path import Pathfinder

class TestBFS(unittest.TestCase):
    def setUp(self):
        self.world = GridWorld(5, 5)
        self.pf = Pathfinder(self.world)

    def test_find_path_simple(self):
        # No walls, path should be Manhattan distance
        path = self.pf.find_path(self.world.start, self.world.goal)
        self.assertIsNotNone(path)
        self.assertEqual(path[0], self.world.start)
        self.assertEqual(path[-1], self.world.goal)
        # Shortest path in 5x5 from (0,0) to (4,4) is 8 steps (9 positions)
        self.assertEqual(len(path), 9)

    def test_no_path(self):
        # Block the goal
        self.world.place_wall(Position(3, 4))
        self.world.place_wall(Position(4, 3))
        # Wait, (4,4) is goal. Neighbors are (3,4) and (4,3).
        # If I block them, no path.
        
        path = self.pf.find_path(self.world.start, self.world.goal)
        self.assertIsNone(path)

    def test_start_is_goal(self):
        path = self.pf.find_path(self.world.start, self.world.start)
        self.assertEqual(path, [self.world.start])

    def test_wall_obstacle(self):
        # Simple obstacle
        # S . .
        # # # .
        # G . .
        world = GridWorld(3, 3, start=Position(0, 0), goal=Position(2, 0))
        world.place_wall(Position(1, 0))
        world.place_wall(Position(1, 1))
        
        pf = Pathfinder(world)
        path = pf.find_path(world.start, world.goal)
        
        self.assertIsNotNone(path)
        # Path must go around: (0,0)->(0,1)->(0,2)->(1,2)->(2,2)->(2,1)->(2,0)
        # Length 7
        self.assertEqual(len(path), 7)

if __name__ == '__main__':
    unittest.main()
