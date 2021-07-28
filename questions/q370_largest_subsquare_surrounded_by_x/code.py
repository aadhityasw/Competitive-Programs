class Solution:
    def largestSubsquare(self,N,A):

        # Initialize a table to store (bottom, right)
        # bottom - the number of concecutive `X` from that cell in bottom direction
        # right - the number of concecutive `X` from that cell in right direction
        table = [[None for _ in range(N+1)] for _ in range(N+1)]

        # Initialize the last row and column to be (0, 0) for even computation of all cells in the matrix
        for i in range(N+1) :
            table[i][N] = (0, 0)
            table[N][i] = (0, 0)

        # Fill the tables
        for i in range(N-1, -1, -1) :
            for j in range(N-1, -1, -1) :
                if A[i][j] == 'X' :
                    table[i][j] = (
                        1 + table[i+1][j][0],
                        1 + table[i][j+1][1]
                    )
                else :
                    table[i][j] = (0, 0)

        # Initialize a variable to store the maximum size
        max_size = 0

        # Find the maximum size
        for i in range(N-1, -1, -1) :
            for j in range(N-1, -1, -1) :
                if A[i][j] == 'X' :
                    # Find the current size of the boundary that can be formed
                    cur_size = min(table[i][j])
                    
                    while cur_size > max_size :
                        # Check if the bottom row and the right column can also accomodate a box of this size
                        if table[i+cur_size-1][j][1] >= cur_size and table[i][j+cur_size-1][0] >= cur_size :
                            max_size = max(
                                max_size,
                                cur_size
                            )
                        cur_size -= 1
    
        # Return the maximum possible size
        return max_size





import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        a=[]
        for i in range(N):
            s=list(map(str,input().strip().split()))
            a.append(s)
        ob=Solution()
        print(ob.largestSubsquare(N,a))
