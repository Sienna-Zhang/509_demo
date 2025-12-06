from .position import Position

class Agent:
    def __init__(self, world, pos=None):
        self.world = world
        self.at = pos if pos else world.start

    def can_move_to(self, pos):
        return self.world.in_bounds(pos) and self.world.passable(pos)

    def step(self, direction):
        """
        Moves the agent in the given direction ('up', 'down', 'left', 'right').
        Returns True if moved, False otherwise.
        """
        deltas = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        
        if direction not in deltas:
            return False
            
        dr, dc = deltas[direction]
        target_pos = Position(self.at.row + dr, self.at.col + dc)
        
        if self.can_move_to(target_pos):
            self.at = target_pos
            return True
        return False

    def reset(self, pos):
        self.at = pos
