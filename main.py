import sudokuSolver as s
import sudokuSolverV2 as sv
from unittest import main
import copy

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
print("Original One")
s.solveSudoku(game_board2)

print("Updated V2")

game_board3 = copy.deepcopy(game_board1)

# need to add test to full board!
sv.solveSudoku(game_board3)


