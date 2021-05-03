class Solution:

    def getCandidates(self, r, c) :
        positions = [
            (r-1, c),
            (r, c-1),
            (r, c+1),
            (r+1, c)
        ]
        return [(i, j) for (i, j) in positions if 0<=i<self.N and 0<=j<self.M and self.A[i][j]== 1 and not self.visited[i][j]]
        


    def shortestDistance(self,N,M,A,X,Y):

        self.visited = [[False for _ in range(M)] for _ in range(N)]
        self.A = A
        self.M = M
        self.N = N
        queue = []

        # Breadth First Search
        if A[0][0] == 1 :
            queue.append((0, 0, 0))
            self.visited[0][0] = True

        if X == Y == 0 :
            return 0
        
        while len(queue) > 0 :
            (r, c, w) = queue.pop(0)

            for (i, j) in self.getCandidates(r, c) :
                queue.append((i, j, w+1))
                self.visited[i][j] = True
                if X == i and Y == j :
                    return (w+1)
        
        return -1



import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,input().strip().split()))
            a.append(s)
        x,y=map(int,input().strip().split())    
        ob=Solution()
        print(ob.shortestDistance(N,M,a,x,y))
