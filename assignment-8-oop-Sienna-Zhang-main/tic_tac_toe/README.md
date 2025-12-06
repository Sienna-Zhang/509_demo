# Tic-Tac-Toe Game

## 1. Problem Description
This project implements a command-line version of the classic Tic-Tac-Toe game using Python. It demonstrates Object-Oriented Programming (OOP) principles and a modular architecture. Key features include:
- A `Board` class to manage the grid state and check for winners.
- A `Player` class hierarchy supporting both Human and Random AI players.
- A game loop that handles turns, input validation, and game termination.
- Data logging to record game outcomes.

## 2. How to Run the Solution

### Dependencies
- Python 3
- (Optional) Virtual Environment

### Setup
1. Navigate to the `tic_tac_toe` directory.
2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

### Running the Game
To start a new game:
```bash
python main.py
```

### Running Tests
To verify the win-checking logic:
```bash
python tests/test_check_winner.py
```

## 3. Associate Explanations

### Architecture
The project follows a simplified MVC pattern:
- **Models** (`models/`): `Board` encapsulates the 3x3 grid and win logic. `Player` defines how moves are chosen.
- **Controller** (`utils/game_logic.py`): Manages the flow of the game, alternating turns between players.
- **View**: The console acts as the view, rendering the board state via `Board.draw_board()`.

### Key Components
- **`board.py`**: Contains the `Board` class with methods `make_move`, `check_winner`, and `check_draw`.
- **`player.py`**: Defines `HumanPlayer` (gets input from stdin) and `RandomPlayer` (selects random valid moves).
- **`record_data.py`**: Logs the results of each game (winner, starting player) to a CSV file.

## 4. Sample Input and Output

**Game Session Example:**

```text
Current Board:
  0 1 2
0 . . .
1 . . .
2 . . .

Player X's turn.
Enter row and column (e.g., 0 0): 1 1

Current Board:
  0 1 2
0 . . .
1 . X .
2 . . .

Player O's turn.
Player O chose: 0 0

Current Board:
  0 1 2
0 O . .
1 . X .
2 . . .

...

Player X wins!
```
