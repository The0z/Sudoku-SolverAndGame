# Rewritten SudokuSolver with Improvements made and unused code removed.
# Looked at multiple internet solutions to get a better idea.

# Check if all nums in row are Unique
from sudokuSolver import isPredefined, printSolution, solveSudokuUtil


def unique_in_row(board, row, num):
    '''
        Used to check if a row has all unique numbers
    '''
    for i in range(9):
        # if num already exists in row, not unique
        if(board[row][i] == num):
            return False    
    # Else return num is unique to row
    return True

# Check if all nums in column are Unique
def unique_in_col(board, col, num):
    '''
        Used to check if a column has all unique numbers
    '''
    for i in range(9):
        # if num already exits in row, not unique
        if(board[i][col] == num):
            return False
    # Else return num is unique to row
    return True

# Check if Squares are Unique
def unique_in_3x3square(board, row, col, num):
    '''
        used to determine if all numbers in a  3x3 square are unique
    '''
    # Determine the start of a grid. 
    # Think Grid is 3x3 so row - row%3 will give the right location
    # Example: row = 2 --> row - row%3 = 2 - 2 = row 0 is start of grid
    # Example2: row = 5 --> 5 - 5%3 = 5 -2 = row 3 is start of grid
    x = row - row%3
    y = col - col%3

    for i in range(x, x+3):
        for j in range(y, y+3):
            # if num already exists in square return false
            if(board[x][y] == num):
                return False
    # Otherwise return true
    return True

def isUniqueNum(board, row, col, num):
    '''
        Function that checks if number is unique within rows, columns, and
        3by3 grid.
    '''
    # Set up this way for easier testing of methods.
    if(not unique_in_row(board, row, num)):
        return False
    if(not unique_in_col(board, col, num)):
        return False
    if(not unique_in_3x3square(board, row, col, num)):
        return False 

    return True

# Check if grid spot is already predefined
def isOccupied(board, row, col):
    '''
        Function to check if spot on board is full or empty.
        Return True if not empty
    '''
    #print("Entered isOccupied ", board[row][col])
    if(board[row][col] != 0):
        return True
    return False

# increment x and y axis
def increment(row, col):
    '''
        increases column and row values to prevent them from going out of bounds
    '''
    col = col + 1
    if(col >= 9):
        col = 0
        if(row < 8):
            row = row + 1

    return row, col

# SolveSudokuUtil
def solveSudokuUtil(board, row, col):
    if(row + col == 16):
        return True
    
    while(isOccupied(board, row, col)):
        row, col = increment(row, col)

    for num in range(1,10):
        if(isUniqueNum(board, row, col, num)):
            board[row][col] = num
            new_row, new_col = increment(row, col)
            if(solveSudokuUtil(board, new_row, new_col)):
                return True
            board[row][col] = 0 
    # Return False if cannot find a solution
    return False

def printSolution(board):
    for row in range(9):
        for col in range(9):
            print(str(board[row][col]) + " ", end=' ')
        print()


# SolveSudoku Main Function
def solveSudoku(board):
    '''
        Main function that runs all the others
    '''
    if(solveSudokuUtil(board, row=0, col=0)):
        print("Solution Found")
        printSolution(board)
    else:
        print("No Solution")
    

