class Solution:

    def getPositions(self, i, j) :
        return ([
            (i-1, j-1),
            (i-1, j),
            (i-1, j+1),
            (i, j-1),
            (i, j+1),
            (i+1, j-1),
            (i+1, j),
            (i+1, j+1)
        ])

    def recursiveMark(self, i, j, marker) :


        # Mark the current cell
        self.grid[i][j] = marker
        
        # Travel to all adjoining land cells
        for (a, b) in self.getPositions(i, j) :
            if (a >= 0) and (a < self.m) and (b >= 0) and (b < self.n) and (self.grid[a][b] != 0) and (self.grid[a][b] != marker) :
                self.recursiveMark(a, b, marker)
                

    def numIslands(self, grid):

        # Initialize the marker
        marker = 2

        self.m = len(grid)
        self.n = len(grid[0])

        # Convert the grid to numbers
        for i in range(self.m) :
            for j in range(self.n) :
                grid[i][j] = ord(grid[i][j]) - 48
        
        self.grid = grid

        for i in range(self.m) :
            for j in range(self.n) :
                if self.grid[i][j] == 1 :
                    self.recursiveMark(i, j, marker)
                    marker += 1
                
        return (marker - 2)



if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            a = list(input().split())
            grid.append(a)
        obj = Solution()
        ans = obj.numIslands(grid)
        print(ans)
