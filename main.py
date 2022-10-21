# main python file containing the files

from concurrent.futures.process import _threads_wakeups

from pyparsing import col


class sudokuSolver:
    '''
    class used to contain the methods that will be used to solve and initialise the sudoku
    using a class to make it more compatible later
    '''
    def __init__(self):
        '''
        initialisor function
        '''
        self.board = [] # the main sudo board is an array of 9 sub arrays, 
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
        column_array =[self.board[x][column] for x in self.board]
        for item in column_array:
            if column_array.count(item) > 1 and item != "x":
                return False
        
        #final return statement
        return True

    #TODO make the function that checks the area
