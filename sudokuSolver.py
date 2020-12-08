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

# Creating Grid
grid1 = (0, 0, 0, 1, 1, 1, 2, 2, 2)
grid2 = (3, 3, 3, 4, 4, 4, 5, 5, 5)
grid3 = (6, 6, 6, 7, 7, 7, 8, 8, 8)

grid = ( grid1, grid1, grid1, grid2, grid2, grid2, grid3, grid3, grid3)
grid_start = {
    0 : (0, 0),
    1 : (0, 3),
    2 : (0, 6),
    3 : (3, 0),
    4 : (3, 3),
    5 : (3, 6),
    6 : (6, 0),
    7 : (6, 3),
    8 : (6, 6)
}

'''
    Checks if row and column is unique.
'''
def isRowAndColUnique(game_board, x, y, num):
    # -2 to account for length check later on
    count_row = -2
    count_col = -2
    row_set = {num}
    col_set = {num}
    
    # First Count number of -1's in the row and column
    # Create the set of Unique Numbers
    for i in range(9):
        if(game_board[x][i] == 0):
            count_row = count_row + 1
        if(game_board[i][y] == 0):
            count_col = count_col + 1
        row_set.add(game_board[x][i])
        col_set.add(game_board[i][y])

    # Check if the value in row and column is unique
    if((len(row_set) + count_row) != 9):
        return False
    if ((len(col_set) + count_col) != 9):
        return False

    return True

'''
    Function used to determined which grid the number is in
    square grids assumed
'''
def isUnique3by3Grid(game_board, x, y, num):
    # Find the starting x and why value
    arr = grid_start.get(grid[x][y])   
    x_start = arr[0]
    y_start = arr[1]
    count_undef = -2
    grid_set = {num}

    # Check numbers for uniqueness
    for i in range(3):
        for j in range(3):
            if(game_board[x_start+i][y_start+j] == 0):
                count_undef = count_undef + 1
            grid_set.add(game_board[x_start+i][y_start+j])   
    

    #print(grid_set)
    #print(count_undef)             

    # return true if all the numbers are unique
    if((len(grid_set) + count_undef) == 9):
        return True

    # Return false if numbers aren't unique
    return False

'''
    Checks if rows, columns, and grids all have unique numbers - if so return true.
'''
def isUniqueAnswer(game_board, x, y, num):
    # Check if grid is unique
    if(not isUnique3by3Grid(game_board,x,y,num)):
        #print("Failed Column")
        return  False
    
    # Check if row and col is unique
    if(not isRowAndColUnique(game_board,x,y,num)):
       #print("Failed Row")
       return False
    
    # all above is unique
    #print("True in isUnique Answer")
    return True

'''
    Purpose is to check if number was already predifined. If so return True, else False.
'''
def isPredefined(orig_board, x, y):
    if(orig_board[x][y] != 0):
        return True
    else:
        return False

'''
    Increments x and y to move across the sudoku board board
'''
def increment(x, y, n):
    y = y + 1
    if (y >= 9):
        y = 0
        if(x < 8):
            x = x + 1
    return x, y

def decrement(x, y, n):
    y = y - 1
    if(y < 0):
        y = 8
        if(x > 0):
            x = x - 1
    return x, y

'''
    Recursive function used to solve the Sudoku Board
'''
def solveSudokuUtil(game_board, x, y, n):
    # Create Shallow Copy to be used to confirm we don't overwrite existing numbers. 
    #Potential an array with just the index locations would be more efficient, but this will do for now.
    orig_board = game_board.copy()

    #Create Exit Case:
    if(x + y == 16):
        return True
    else:
        while(isPredefined(game_board,x,y)):
            x, y = increment(x,y,n)
        for num in range(10):
            if(isUniqueAnswer(game_board, x, y, num)):
                game_board[x][y] = num
                x_new , y_new = increment(x,y,n)
                if(solveSudokuUtil(game_board,x,y,n)):
                    return True
                game_board[x][y] = 0        
        return False
        

    





    
    # for num in range(1,10):
    #     if(isPredefined(game_board, x,y)):
    #         new_x, new_y = increment(x,y,n)
    #         solveSudokuUtil(game_board, new_x, new_y, n, pos+1)

    #     if(isUniqueAnswer(game_board, x, y, num)):
    #         new_x, new_y = increment(x, y, n)
    #         game_board[x][y] = num
    #         # Begin the recursion
    #         if(solveSudokuUtil(game_board, new_x, new_y, n, pos+1)):
    #             return True
    #         # if the above doesn't return true we need to backtrack!
    #         game_board[x][y] = 0
    # # Failed to find a solution!
    # return False        

'''
    Utlity Function to print sudoku board    
'''
def printSolution(game_board):
    for x in range(9):
        for y in range(9):
            print(str(game_board[x][y]) + " ", end=' ')
        print()

'''
    Main program that begins the solving and starts the printing process
'''
def solveSudoku(game_board):

    solve_result = solveSudokuUtil(game_board, x=0, y=0, n=9)

    if(solve_result == True):
        print("THE SOLVED SOLUTION IS")
        printSolution(game_board)
    else:
        print("Error, Unsolvable or Solution Cannot be Found")