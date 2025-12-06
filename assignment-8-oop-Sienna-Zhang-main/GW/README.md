# Grid World Navigation

## 1. Problem Description
This project implements a Grid World navigation system where an agent must find the shortest path from a starting point to a goal while avoiding obstacles (walls). It demonstrates:
- Object-Oriented Programming (OOP) principles with classes for Position, GridWorld, Agent, and Pathfinder.
- Breadth-First Search (BFS) algorithm for finding the shortest path in an unweighted grid.
- Console-based visualization of the grid and the agent's movement.

## 2. How to Run the Solution

### Dependencies
- Python 3 (Standard Library only)

### Running the Demo
To see the agent find a path and move to the goal:

```bash
python demo.py
``` 

### Running Tests
To verify the correctness of the components and the BFS algorithm:

```bash
python -m unittest discover tests
``` 

## 3. Associate Explanations

### Algorithm
The `Pathfinder` class uses **Breadth-First Search (BFS)** to guarantee the shortest path in an unweighted grid. It explores neighbors layer by layer, keeping track of visited positions to avoid cycles.

### Key Components
- **`position.py`**: A value object representing `(row, col)` coordinates. Handles equality and neighbor generation.
- **`grid_world.py`**: Manages the grid dimensions, wall locations, and rendering. Checks if a position is valid and passable.
- **`agent.py`**: Represents the moving entity. It can take steps in cardinal directions if the move is valid.
- **`path.py`**: Contains the BFS logic to compute the sequence of positions from start to goal.

## 4. Sample Input and Output

**Example Output from `demo.py`:**

```text
--- Initial World ---
. . . . . 
. # # # . 
. . S # . 
. . . . . 
. . . G . 

Finding path from (2, 2) to (4, 3)...
Path found! Length: 5 steps.

--- Moving Agent ---
Step 0: Agent at (2, 2)
Step 1: Agent at (2, 1)
Step 2: Agent at (3, 1)
Step 3: Agent at (3, 2)
Step 4: Agent at (3, 3)
Step 5: Agent at (4, 3)
Goal Reached!
```
