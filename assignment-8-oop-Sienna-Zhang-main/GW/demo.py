import time
import os
import sys

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from GW.position import Position
from GW.grid_world import GridWorld
from GW.agent import Agent
from GW.path import Pathfinder

def main():
    # 1. Build a 5x7 world
    rows, cols = 5, 7
    start = Position(0, 0)
    goal = Position(4, 6)
    
    world = GridWorld(rows, cols, start=start, goal=goal)
    
    # Add some walls
    walls = [
        Position(1, 1), Position(1, 2), Position(1, 3),
        Position(2, 3), Position(3, 3),
        Position(3, 5), Position(4, 5)
    ]
    for w in walls:
        world.place_wall(w)
        
    print("Initial World:")
    world.render()
    print("\n" + "="*20 + "\n")
    
    # 2. Find path
    pf = Pathfinder(world)
    path = pf.find_path(start, goal)
    
    if path:
        print(f"Path found! Length: {len(path)}")
        print(f"Path: {path}")
        
        print("\nWorld with Path:")
        world.render(path=path)
        print("\n" + "="*20 + "\n")
        
        # 3. Move Agent
        agent = Agent(world, start)
        print("Agent Moving:")
        
        for step_pos in path:
            # Determine direction (just for simulation, we can teleport or calculate direction)
            # Here we just teleport the agent to the next step in the path for visualization
            agent.reset(step_pos)
            
            # Clear screen (optional, might flicker in some terminals)
            # os.system('cls' if os.name == 'nt' else 'clear')
            
            print(f"Agent at: {agent.at}")
            world.render(path=path, agent=agent)
            print("-" * 20)
            time.sleep(0.5)
            
    else:
        print("No path found!")

if __name__ == "__main__":
    main()
