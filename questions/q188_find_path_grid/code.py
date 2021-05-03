class Solution:
    
    def getCandidates(self, r, c) :
        positions = [
            (r-1, c),
            (r, c-1),
            (r, c+1),
            (r+1, c)
        ]
        return [(i, j) for (i, j) in positions if 0<=i<self.M and 0<=j<self.N and self.grid[i][j] > 0 and not self.visited[i][j]]
        
        
    def is_Possible(self, grid):
        
        self.grid = grid
        self.M = len(grid)
        self.N = len(grid[0])
        self.visited = [[False for _ in range(self.N)] for _ in range(self.M)]
        stack = []
        
        s = None
        for i in range(self.M) :
            for j in range(self.N) :
                if grid[i][j] == 1 :
                    s = [i, j]
                    break
            if s is not None :
                break

        # Depth First Search
        if grid[s[0]][s[1]] == 1 :
            stack.append((s[0], s[1]))
            self.visited[s[0]][s[1]] = True
        
        while len(stack) > 0 :
            (r, c) = stack.pop()

            for (i, j) in self.getCandidates(r, c) :
                stack.append((i, j))
                self.visited[i][j] = True
                if grid[i][j] == 2 :
                    return True
        
        return False




if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        grid = []
        for _ in range(n):
            a = list(map(int, input().split()))
            grid.append(a)
        obj = Solution()
        ans = obj.is_Possible(grid)
        if(ans):
            print("1")
        else:
            print("0")
