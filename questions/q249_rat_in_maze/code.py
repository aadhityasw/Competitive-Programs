class Solution:

    def findCandidates(self, arr, n, cur_position) :

        x, y = cur_position

        # This order resolves the problem of sorting the final results
        options = [
            (x+1, y, 'D'), (x, y-1, 'L'), 
            (x, y+1, 'R'), (x-1, y, 'U')
        ]
        candidates = []

        for option in options :
            if (0 <= option[0] < n) and (0 <= option[1] < n) and (not self.visited[option[0]][option[1]]) and (arr[option[0]][option[1]] != 0) :
                candidates.append(option)
        
        return candidates


    def findValidPaths(self, arr, n, cur_position, cur_path) :

        x, y = cur_position
        self.visited[x][y] = True

        if x == n-1 == y :
            self.validPaths.append(cur_path)
        else :
            for candidate in self.findCandidates(arr, n, cur_position) :
                direction = candidate[2]
                self.findValidPaths(arr, n, candidate[:2], cur_path+direction)

        self.visited[x][y] = False



    def findPath(self, m, n):

        # If the first cell is zero we return saying that no path exists
        if m[0][0] == 0 :
            return []
        
        self.validPaths = []
        self.visited = [[False for _ in range(n)] for _ in range(n)]

        # Find the paths
        self.findValidPaths(m, n, (0, 0), "")
        
        return self.validPaths


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
