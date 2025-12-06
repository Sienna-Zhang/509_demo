from collections import deque
from .position import Position

class Pathfinder:
    def __init__(self, world):
        self.world = world

    def find_path(self, start, goal):
        """
        Finds the shortest path from start to goal using BFS.
        Returns a list of Position objects from start to goal, or None if no path exists.
        """
        if not self.world.passable(start) or not self.world.passable(goal):
            return None
            
        queue = deque([(start, [start])])
        visited = {start}
        
        nodes_expanded = 0
        
        while queue:
            current_pos, path = queue.popleft()
            nodes_expanded += 1
            
            if current_pos == goal:
                # print(f"Nodes expanded: {nodes_expanded}")
                return path
            
            for neighbor in current_pos.neighbors_4():
                if self.world.in_bounds(neighbor) and self.world.passable(neighbor) and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
                    
        return None
