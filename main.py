import sudokuSolver as s
from unittest import main

## Enable to Run Unit Tests
# main(module='test_module', exit=False)

## Enable for normal Running

# Sudoku Board to Solve
game_board1 = [[3, 0, 6, 5, 0, 8, 4, 0, 0], 
               [5, 2, 0, 0, 0, 0, 0, 0, 0], 
               [0, 8, 7, 0, 0, 0, 0, 3, 1], 
               [0, 0, 3, 0, 1, 0, 0, 8, 0], 
               [9, 0, 0, 8, 6, 3, 0, 0, 5], 
               [0, 5, 0, 0, 9, 0, 6, 0, 0], 
               [1, 3, 0, 0, 0, 0, 2, 5, 0], 
               [0, 0, 0, 0, 0, 0, 0, 7, 4], 
               [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

game_board2 = [ [0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0] ]


## Solve the Board and Print it Out
s.solveSudoku(game_board1)
## print solution
#s.printSolution(game_board)