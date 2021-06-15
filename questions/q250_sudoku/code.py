class Solution:

    def findNextEmptyCell(self, grid) :
        """
        Given the board, finds the next empty cell if any present, and returns its position
        """
        
        # Find the first empty cell and return its position
        for i in range(9) :
            for j in range(9) :
                if grid[i][j] == 0 :
                    return (i, j)
        
        # In case the whole grid is complete
        return -1, -1

    
    def checkValidity(self, grid, position, ele) :
        """
        Given the grid, an element and the position where it is to be placed, we check if making this move does not violate the conditions of the board
        """

        # Get the co-ordinates
        x, y = position

        # Check in that x row and y column
        for i in range(9) :
            if grid[x][i] == ele :
                return False
            if grid[i][y] == ele :
                return False
        
        # Check in its 3x3 mini grid
        pos_x = 3*(x//3)
        pos_y = 3*(y//3)
        for i in range(pos_x, pos_x+3) :
            for j in range(pos_y, pos_y+3) :
                if grid[i][j] == ele :
                    return False
        
        # If all conditions are satisfied then return True
        return True

    
    #Function to find a solved Sudoku. 
    def SolveSudoku(self,grid):
        x, y = self.findNextEmptyCell(grid)

        if x == -1 or y == -1 :
            return True
        
        for ele in range(1, 10) :
            if self.checkValidity(grid, (x, y), ele) :
                grid[x][y] = ele
                # If it is solvable with this number placed here, then we return successfully
                if self.SolveSudoku(grid) :
                    return True
                # Else we backtrack
                grid[x][y] = 0
        
        return False
        
    
    #Function to print grids of the Sudoku.    
    def printGrid(self,arr):
        final = ""
        for row in arr :
            final += " ".join([str(i) for i in row]) + " "
        print(final)



if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
                
        ob = Solution()
            
        if(ob.SolveSudoku(grid)==True):
            ob.printGrid(grid)
            print()
        else:
            print("No solution exists")
        t = t-1
