# main python file containing the files
from operator import index


class sudokuSolver:
    '''
    class used to contain the methods that will be used to solve and initialise the sudoku
    using a class to make it more compatible later
    '''
    def __init__(self,board):
        '''
        initialisor function
        '''
        self.board = board # the main sudo board is an array of 9 sub arrays, 
                        # all containing 9 items, an item is either a number, 
                        # or a "x" meaning a number to solve
        
    def correct_row(self, row:int) -> bool:
        '''
        input -> self, row: int
        output -> boolean
        desc -> checks the row of the line to check if it is correct, excluding "x"s 
        '''
        check_row = self.board[row]

        # checks if there are more than one of each item in the row
        for item in check_row:
            if check_row.count(item) > 1 and item != "x":
                return False
        
        # final return statement
        return True

    def correct_column(self, column:int) -> bool:
        '''
        input -> self, column:int 
        output -> boolean 
        desc -> takes the integer as the index of the column 
                and returns if the column has duplicates of a number.
        '''
        
        # making the list that represents the column

        # aha the funny
        column_array =[self.board[x][column] for x in range(len(self.board))]
        for item in column_array:
            if column_array.count(item) > 1 and item != "x":
                return False
        
        #final return statement
        return True


    def correct_area(self, area:int) -> bool:
        '''
        input -> area: int
        output -> boolean
        desc -> takes an int, 
                and checks to see if the ares described by the int
                has any duplicate numbers, if not then true else false
        '''
        # array that contains the indexs for the column/row to take
        indexs = [[0,1,2], [3,4,5], [6,7,8],[0,1,2], [3,4,5], [6,7,8],[0,1,2], [3,4,5], [6,7,8]]
        res = [] # array that will contain all the numbers in the area
        area_index = area
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i in indexs[area_index] and j in indexs[area_index]:
                    res.append(self.board[i][j])
        
        # res now contains every number in the area we have to check
        for item in res:
            if res.count(item) > 1 and item != "x":
                return False
        
        return True # final return statement

    def all_correct(self):
        '''
        input -> none
        output -> boolean
        desc -> checks the entire sudoku to see if it breaks any of the functions
            that we previously made
        '''
        # testing each column
        for j in range(len(self.board[0])): 
            if self.correct_column(j) != True:
                return (False, "failed on column {}".format(j))
        
        #testing each row
        for i in range(len(self.board)):
            if self.correct_row(i) != True:
                return (False, "failed on row {}".format(i))
        
        #testing each area
        for k in range(0,9):
            if self.correct_area(k) != True:
                return (False, "failed on area {}".format(k))
        return (True, "Verified all tests")

board = [[1,2,'x','x','x','x','x','x',5],
         ['x','x',2,'x','x','x','x','x','x'],
         ['x','x','x','x','x','x','x','x','x'],
         ['x','x','x','x','x','x','x','x','x'],
         ['x','x','x','x','x','x','x','x','x'],
         ['x','x','x','x','x','x','x','x','x'],
         ['x','x','x','x','x','x','x','x','x'],
         ['x','x','x','x','x','x','x','x','x'],
         ['x','x','x','x','x','x','x','x','x'],]
sudoku = sudokuSolver(board=board)
print(sudoku.all_correct())
