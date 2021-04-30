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

    def DFS(self, i, j, marker) :

        queue = [(i, j)]

        while len(queue) > 0 :

            (r, c) = queue.pop()
            self.grid[r][c] = marker

            # Travel to all adjoining land cells
            for (a, b) in self.getPositions(r, c) :
                if (a >= 0) and (a < self.m) and (b >= 0) and (b < self.n) and (self.grid[a][b] == 1) :
                    queue.append((a, b))
                

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
                    self.DFS(i, j, marker)
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
