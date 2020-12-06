import unittest
import sudokuSolver as s

game_board = [ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
               [5, 2, 0, 0, 0, 0, 0, 0, 0], 
               [0, 8, 7, 0, 0, 0, 0, 3, 1], 
               [0, 0, 3, 0, 1, 0, 0, 8, 0], 
               [9, 0, 0, 8, 6, 3, 0, 0, 5], 
               [0, 5, 0, 0, 9, 0, 6, 0, 0], 
               [1, 3, 0, 0, 0, 0, 2, 5, 0], 
               [0, 0, 0, 0, 0, 0, 0, 7, 4], 
               [0, 0, 5, 2, 0, 6, 3, 0, 0] ]


# class used to test cases
class UnitTests(unittest.TestCase):
    # Begin Testing unique3by3 Grid Function
    def test_grid1(self):
        actual =  s.isUnique3by3Grid(game_board, x=0, y=1, num=4)
        expected = True
        self.assertEqual(actual, expected, 'Grid1 Test Failed')
    
    def test_grid2(self):
        actual =  s.isUnique3by3Grid(game_board, x=1, y=5, num=5)
        expected = False
        self.assertEqual(actual, expected, 'Grid2 Test Failed')
    
    def test_grid3(self):
        actual =  s.isUnique3by3Grid(game_board, x=2, y=6, num=9)
        expected = True
        self.assertEqual(actual, expected, 'Grid3 Test Failed')
    
    def test_grid4(self):
        actual =  s.isUnique3by3Grid(game_board, x=4, y=1, num=2)
        expected = True
        self.assertEqual(actual, expected, 'Grid4 Test Failed')
    
    def test_grid5(self):
        actual =   s.isUnique3by3Grid(game_board, x=3, y=3, num=7)
        expected = True
        self.assertEqual(actual, expected, 'Grid5 Test Failed')
    
    def test_grid6(self):
        actual =  s.isUnique3by3Grid(game_board, x=3, y=8, num=6)
        expected = False
        self.assertEqual(actual, expected, 'Grid6 Test Failed')
    
    def test_grid7(self):
        actual =  s.isUnique3by3Grid(game_board, x=8, y=1, num=1)
        expected = False
        self.assertEqual(actual, expected, 'Grid7 Test Failed')
    
    def test_grid8(self):
        actual =  s.isUnique3by3Grid(game_board, x=6, y=4, num=8)
        expected = True
        self.assertEqual(actual, expected, 'Grid8 Test Failed')
    
    def test_grid9(self):
        actual =  s.isUnique3by3Grid(game_board, x=8, y=8, num=3)
        expected = False
        self.assertEqual(actual, expected, 'Grid9 Test Failed')

    #Begin Testing Row and Column Testing

if __name__ == "__main__":
    unittest.main()

# Testing Unique3by3Grid -- Passed all the below
#print("should be True:", s.isUnique3by3Grid(game_board, x=0, y=1, num=4)) 
#print("should be False:", s.isUnique3by3Grid(game_board, x=1, y=5, num=5))
#print("should be True:", s.isUnique3by3Grid(game_board, x=2, y=6, num=9))
#print("should be True:", s.isUnique3by3Grid(game_board, x=4, y=1, num=2))
#print("should be True:", s.isUnique3by3Grid(game_board, x=3, y=3, num=7))
#print("should be False:", s.isUnique3by3Grid(game_board, x=3, y=8, num=6))
#print("should be False:", s.isUnique3by3Grid(game_board, x=8, y=1, num=1))
#print("should be True:", s.isUnique3by3Grid(game_board, x=6, y=4, num=8))
#print("should be False:", s.isUnique3by3Grid(game_board, x=8, y=8, num=3))
