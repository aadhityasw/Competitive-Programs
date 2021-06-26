class Solution:

    def getValidPositions(self, position, dimensions) :
        """
        Given a cell position, we return the co-ordinates of all the neighboring cells
        """

        # Destructure the position and dimensions of the board
        r, c = dimensions
        i, j = position

        possible_positions = [
            (i+1, j), (i-1, j),
            (i, j+1), (i, j-1)
        ]
        candidate_positions = []
        
        for pos in possible_positions :
            if 0 <= pos[0] < r and 0 <= pos[1] < c :
                candidate_positions.append(pos)
        
        return candidate_positions


    def color(self, position, grid, board, code) :
        """
        Given a position to color code and the color, we paint that position, and its linked X's
        """

        # Color the current cell
        board[position[0]][position[1]] = code

        # Use DFS to color its neighboring cells
        for pos in self.getValidPositions(position, (len(grid), len(grid[0]))) :
            (i, j) = pos
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) :
                if grid[i][j] == 'X' and board[i][j] == 0 :
                    self.color((i, j), grid, board, code)

    
    #Function to find the number of 'X' total shapes.
    def xShape(self, grid):
        n = len(grid)
        m = len(grid[0])
        board = [[0 for _ in range(m)] for _ in range(n)]
        num_groups = 0

        for i in range(n) :
            for j in range(m) :
                if grid[i][j] == 'X' and board[i][j] == 0 :
                    num_groups += 1
                    self.color((i, j), grid, board, num_groups)
        
        return num_groups



if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = [['#' for i in range(m)] for j in range(n)]
        for i in range(n):
            s = input().strip()
            for j in range(m):
                grid[i][j] = s[j]
        obj = Solution()
        ans = obj.xShape(grid)
        print(ans)
