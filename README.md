# Sudoku Solver

This is a Sudoku solver implemented in Python. It uses a backtracking algorithm to find solutions to Sudoku puzzles.

## How to Run the Code

1.  Make sure you have Python installed on your system.
2.  Save the code in a file named `solver.py`.
3.  Run the code from the command line using the command: `python solver.py`

## Input File Format

The Sudoku board is represented as a list of lists, where each inner list represents a row in the board. Empty cells are represented by 0. For example, the following represents an empty Sudoku board:

```
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
```

You can modify the `board` variable in the `solver.py` file to solve different Sudoku puzzles.

## Test Input Files

The following test input files are provided:

*   `test_input_easy.txt`: An easy Sudoku puzzle.
*   `test_input_medium.txt`: A medium Sudoku puzzle (no solution).
*   `test_input_hard.txt`: A hard Sudoku puzzle.

To use these files, run the solver with the command: `python3 solver.py <filename>`.

## Functions

*   `print_board(board)`: Prints the Sudoku board to the console in a user-friendly format.
*   `find_empty(board)`: Finds the next empty cell (represented by 0) in the board and returns its row and column indices as a tuple. If there are no empty cells, it returns `None`.
*   `valid(board, number, pos)`: Checks if a given number is valid to be placed in a given position on the board, according to Sudoku rules.
*   `solve_board(board)`: Solves the Sudoku board using a backtracking algorithm. It recursively tries placing numbers in empty cells until a valid solution is found or all possibilities have been exhausted.
