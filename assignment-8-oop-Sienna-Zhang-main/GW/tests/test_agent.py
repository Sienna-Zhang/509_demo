import unittest
import sys
import os

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from GW.position import Position
from GW.grid_world import GridWorld
from GW.agent import Agent

class TestAgent(unittest.TestCase):
    def setUp(self):
        self.world = GridWorld(5, 5)
        self.agent = Agent(self.world)

    def test_init(self):
        self.assertEqual(self.agent.at, self.world.start)
        
        p = Position(2, 2)
        agent2 = Agent(self.world, p)
        self.assertEqual(agent2.at, p)

    def test_step_valid(self):
        # Start at (0,0). Right is (0,1), Down is (1,0)
        self.assertTrue(self.agent.step('right'))
        self.assertEqual(self.agent.at, Position(0, 1))
        
        self.assertTrue(self.agent.step('down'))
        self.assertEqual(self.agent.at, Position(1, 1))

    def test_step_invalid_boundary(self):
        # Start at (0,0). Up is (-1,0) -> Invalid
        self.assertFalse(self.agent.step('up'))
        self.assertEqual(self.agent.at, Position(0, 0))

    def test_step_invalid_wall(self):
        wall_pos = Position(0, 1)
        self.world.place_wall(wall_pos)
        
        self.assertFalse(self.agent.step('right'))
        self.assertEqual(self.agent.at, Position(0, 0))

    def test_reset(self):
        self.agent.step('right')
        self.assertNotEqual(self.agent.at, Position(0, 0))
        self.agent.reset(Position(0, 0))
        self.assertEqual(self.agent.at, Position(0, 0))

if __name__ == '__main__':
    unittest.main()
