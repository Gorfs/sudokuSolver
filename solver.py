# following along the tech with tim tutorial

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
    desc -> goes through the board and tries to find the next empty space
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j
    return None  # if no empty spaces are found


def valid(board: list, number: int, pos: (int, int)) -> bool:
    """
    input: board: list, number being tested: int, position being tested: list
    output: boolean
    desc -> checks to see if the number entered in the position entered is valid in the board
    """

    # checking the row
    if board[pos[0]].count(number) > 0:
        return False

    # checking the column
    column = []
    for line in board:
        column.append(line[pos[1]])
    if column.count(number) > 0:
        return False

    # checking area
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    box_arr = []
    for i in range(len(board)):
        if (i // 3) == box_y:
            for j in range(len(board[i])):
                if (j // 3) == box_x:
                    box_arr.append(board[i][j])
    if box_arr.count(number) > 0:
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
        print(row, col)

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve_board(board):
                return True
            board[row][col] = 0
    return False


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
print_board(board)
print("")
print(solve_board(board))
print_board(board)
