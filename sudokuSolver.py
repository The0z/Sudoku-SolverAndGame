# Learn to solve Sudoku using back tracking
# Backtracking - technique for solving problems recursively one step at a time and 
# removing failed solutions. Basically backtrack when you find solution doesn't work
# 
# Benefits - faster than trying every single combination of numbers
# https://www.geeksforgeeks.org/backtracking-algorithms/
# Explains the need for performance --> performance = currency
# https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/
# 


# Sudoku 9x9 - Rules - Rows and Columns must contain unique numbers. 3x3 squares must contain
# unique numbers
# Recursive function is the best option.

# checks if rows, columns, and grids all have unique numbers - if so return true.
# can break this function up
def isUniqueAnswer(game_board, x, y, num, n):
    count_row = 0;
    count_col = 0;
    
    # First Count number of -1's in the row and column
    for i in range(8):
        if(game_board[i][y] == -1):
            count_row = count_row + 1
        if(game_board[x][i] == -1):
            count_col = count_col + 1

    # # Check if the value in row is unique
    # num_row = set(game_board[x][y])

    # # Check if value in row is unique  
    
    # for col in range(8):
    #    if() 
    # # check if column is unique
    # for row in range(8):

    # check if grid is unique
    # all above is unique
    return True

# Purpose is to check if number was already predifined. If so return True, else False.
def isPredefined(orig_board, x, y):
    if(orig_board[x][y] != -1):
        return True
    else:
        return False

# Increments x and y to move across the board
def increment(x, y):
    x = x + 1
    if (x == 9):
        x = 0
        y = y + 1
    return x, y

def solveSudoku(game_board, x, y, n, pos):
    # Create Shallow Copy to be used to confirm we don't overwrite existing numbers. 
    # Potential an array with just the index locations would be more efficient, but this will do for now.
    orig_board = game_board.copy()

    # If all the Sodoku numbers are filled end recursive function
    if (pos == n**2):
        return True

    # First Check if spot is predefined, move on to next one if that is the case
    if(isPredefined(orig_board, x, y)):
        new_x, new_y = increment(x, y)
        if(solveSudoku(game_board, new_x, new_y, n, pos+1)):
            return True
    
    for num in range(1,10):
        if(isUniqueAnswer(game_board, x, y, num, n)):
            game_board[x, y] = num
            new_x, new_y = increment(x, y)
            # Begin the recursion
            if(solveSudoku(game_board, new_x, new_y, n, pos+1)):
                return True
            # if the above doesn't return true we need to backtrack!
            game_board[x, y] = -1
    # Failed to find a solution!
    return False        
            
