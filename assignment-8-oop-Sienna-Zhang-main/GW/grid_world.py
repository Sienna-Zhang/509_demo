from .position import Position

class GridWorld:
    def __init__(self, rows, cols, walls=None, start=None, goal=None):
        self.rows = rows
        self.cols = cols
        self.walls = set(walls) if walls else set()
        self.start = start if start else Position(0, 0)
        self.goal = goal if goal else Position(rows - 1, cols - 1)

    def in_bounds(self, pos):
        return 0 <= pos.row < self.rows and 0 <= pos.col < self.cols

    def passable(self, pos):
        return pos not in self.walls

    def is_goal(self, pos):
        return pos == self.goal

    def place_wall(self, pos):
        if self.in_bounds(pos) and pos != self.start and pos != self.goal:
            self.walls.add(pos)

    def remove_wall(self, pos):
        if pos in self.walls:
            self.walls.remove(pos)

    def render(self, path=None, agent=None):
        path_set = set(path) if path else set()
        
        print("+" + "---+" * self.cols)
        for r in range(self.rows):
            line = "|"
            for c in range(self.cols):
                pos = Position(r, c)
                char = " . "
                
                if pos in self.walls:
                    char = " # "
                elif agent and agent.at == pos:
                    char = " A "
                elif pos == self.start:
                    char = " S "
                elif pos == self.goal:
                    char = " G "
                elif pos in path_set:
                    char = " * "
                
                line += char + "|"
            print(line)
            print("+" + "---+" * self.cols)
