import heapq

class Solution:

    def getCandidates(self, r, c) :
        positions = [
            (r-1, c),
            (r, c-1),
            (r, c+1),
            (r+1, c)
        ]
        return [(i, j) for (i, j) in positions if 0<=i<self.M and 0<=j<self.N and not self.visited[i][j]]


    def minimumCostPath(self, grid):

        self.M = len(grid)
        self.N = len(grid[0])
        self.visited = [[False for _ in range(self.N)] for _ in range(self.M)]

        # Breadth First Search

        # Heap is used in place of a queue
        # Each element = (cost from source, -1*row_of_cell, -1*column_of_cell)
        # We multiply -1 with the row and column positions because we would like to prefer the cells closer to the destination if they have equal costs.
        heap = []

        # Visit the initial node
        heapq.heappush(heap, (grid[0][0], 0, 0))
        self.visited[0][0] = True
        
        while True :
            (w, r, c) = heapq.heappop(heap)
            r = r * -1
            c = c * -1

            for (i, j) in self.getCandidates(r, c) :
                heapq.heappush(heap, (w + grid[i][j], -1*i, -1*j))
                self.visited[i][j] = True
                if i == self.M-1 and j == self.N-1 :
                    return (w + grid[i][j])
        
        return -1



if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        grid = []
        for _ in range(n):
            a = list(map(int, input().split()))
            grid.append(a)
        obj = Solution()
        ans = obj.minimumCostPath(grid)
        print(ans)
