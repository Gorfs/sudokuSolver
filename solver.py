import argparse

def print_board(board: list) -> None:
    """
    input -> a list of lists representing the board
    output -> terminal text
    desc -> prints out the board in a nice looking way
    """
    for i in range(len(board)):
        if i % 3 == 0 and not i == 0:  # prints a horizontal line between Layers
            print("--------------------------------------")
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(" " + str(board[i][j]) + " ", end="")
            if j == 8:
                print("")


def find_empty(board: list) -> (int, int):
    """
    input -> list representing sudoku board
    output -> tuple with indexes of next empty space
    desc -> goes through the board and tries to find the next empty space, prioritizing cells with fewer possibilities
    """
    best_pos = None
    min_possibilities = 10  # Start with a value higher than the maximum possible

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                possibilities = 0
                for num in range(1, 10):
                    if valid(board, num, (i, j)):
                        possibilities += 1

                if possibilities < min_possibilities:
                    best_pos = (i, j)
                    min_possibilities = possibilities

    return best_pos


def valid(board: list, number: int, pos: (int, int)) -> bool:
    """
    input: board: list, number being tested: int, position being tested: list
    output: boolean
    desc -> checks to see if the number entered in the position entered is valid in the board
    """
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == number and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == number and pos[0] != i:
            return False

    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == number and (i,j) != pos:
                return False

    return True


def solve_board(board: list) -> bool:
    """
    input -> board: list
    output -> completed board
    desc -> self-explanatory
    """
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve_board(board):
                return True
            board[row][col] = 0
    return False


def read_board_from_file(filename: str) -> list:
    """
    input -> filename: str
    output -> board: list
    desc -> reads the board from the file
    """
    board = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                row = [int(x) for x in line.strip().split(',')]
                board.append(row)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit()
    except ValueError:
        print(f"Error: Invalid data in '{filename}'. Ensure each line contains 9 comma-separated integers.")
        exit()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit()

    if len(board) != 9:
        print(f"Error: Invalid board in '{filename}'. Ensure the board has 9 rows.")
        exit()
    for row in board:
        if len(row) != 9:
            print(f"Error: Invalid board in '{filename}'. Ensure each row has 9 columns.")
            exit()
    return board


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve Sudoku puzzles from a file.')
    parser.add_argument('filename', help='The file containing the Sudoku puzzle.')
    args = parser.parse_args()

    board = read_board_from_file(args.filename)

    print_board(board)
    print("")
    print("solving board...")
    if solve_board(board):
        print("Solution:")
        print_board(board)
    else:
        print("No solution exists")
