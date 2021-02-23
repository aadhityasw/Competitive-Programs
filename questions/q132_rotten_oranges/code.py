class Solution:
    def __init__(self) :
        self.queue = []
        self.max_time = -1
        self.count = 0
        self.m = 0
        self.n = 0
    
    
    def recursiveBFS(self, grid) :
        while len(self.queue) > 0 :
            (i, j, time) = self.queue.pop(0)
            choices = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            
            for choice in choices :
                (r, c) = choice
                if (0 <= r < self.m) and (0 <= c < self.n) :
                    if grid[r][c] == 1 :
                        grid[r][c] = 2
                        self.count -= 1
                        self.queue.append((r, c, (time + 1)))
                        
                        if (time + 1) > self.max_time :
                            self.max_time = (time + 1)
    
    
	def orangesRotting(self, grid):
		self.m = len(grid)
		self.n = len(grid[0])
		
		for i in range(self.m) :
		    for j in range(self.n) :
		        
		        if grid[i][j] == 1 :
		            self.count += 1
		            
		        if grid[i][j] == 2 :
		            self.queue.append((i, j, 0))
		
		self.recursiveBFS(grid)
		
		if self.count == 0 :
		    return self.max_time
		else :
		    return -1


from queue import Queue

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            a = list(map(int, input().split()))
            grid.append(a)
        obj = Solution()
        ans = obj.orangesRotting(grid)
        print(ans)
