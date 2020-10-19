# Author : Adrien Pillou
# Created : 19/10/2020

# A program to solve any sudoku grid with backtracking implemantation

import numpy as np

class Grid:
    def __init__(self, rows, columns):
        self.content = np.zeros((rows, columns))
        self.rows = rows
        self.columns = columns

    def Possible(self, r, c, n): # Check if a number at a (j, i) given position can be marked down
        for i in range(self.rows): # Checking the row
            if (n == self.content[i, c]):
                return False
        for i in range(self.columns): # Checking the column
            if (n == self.content[r, i]):
                return False
        square_start_row = (r//3)*3
        square_start_col = (c//3)*3
        for i in range(3): # Checking the square
            for j in range(3):
                col = square_start_col + i
                row = square_start_row + j
                if (n == self.content[row, col]):
                    return False
        return True

    def Solve(self): # Solve the grid
        completed = self.IsComplete() # Get the next epmty cell (r, c)
        if not completed:
            return True
        else :
            row, col = completed
            for n in range(1, 10): # Iterating through all the possibilities
                if(self.Possible(row, col, n)): # Checking if it's possible to put a number at this position
                    grid.content[row, col] = n
                    if self.Solve():
                        return True
                    grid.content[row, col] = 0
            return False           

    def IsComplete(self): # Check if the grid is completed
        for i in range(9):
            for j in range(9):
                if(self.content[j, i] == 0):
                    return (j, i)
        return None

    def Show(self): # Display a formatted sudoku grid
        print("-------------------------------")
        for j in range(9):
            line = ""
            for i in range(9):
                if(i == 3 or i == 6):
                    line+="|"
                if(i!=0):line+=" "
                line += str( self.content[j, i])
                line+=" "
            print("| "+line+"|")
            if (j==2 or j==5):
                print("-------------------------------")
        print("-------------------------------")

grid = Grid(9, 9)
grid.content =np.matrix([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                         [6, 0, 0, 1, 9, 5, 0, 0, 0],
                         [0, 9, 8, 0, 0, 0, 0, 6, 0],
                         [8, 0, 0, 0, 6, 0, 0, 0, 3],
                         [4, 0, 0, 8, 0, 3, 0, 0, 1],
                         [7, 0, 0, 0, 2, 0, 0, 0, 6],
                         [0, 6, 0, 0, 0, 0, 2, 8, 0],
                         [0, 0, 0, 4, 1, 9, 0, 0, 5],
                         [0, 0, 0, 0, 8, 0, 0, 7, 9]])

grid.Show()
grid.Solve()
grid.Show()