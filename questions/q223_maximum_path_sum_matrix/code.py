class Solution:

    def getPreviousPositions(self, r, c, N) :
        """
        Given the row and column co-ordinates, returns a list of all positions in the matrix from where the current cell can be reached in one step
        """
        
        # Form the choices array
        choices = [
            (i, j) for (i, j) in [(r-1, c-1), (r-1, c), (r-1, c+1)] if 0 <= i < N and 0 <= j < N
        ]

        return choices



    def maximumPath(self, N, Matrix):

        # Initialize the distance matrix to be equal to the inital matrix
        # In the end each cell will holds the length of the longest path from top row till that cell
        distance = [[Matrix[i][j] for j in range(N)] for i in range(N)]

        for i in range(1, N) :
            for j in range(N) :

                # Get the positions in the matrix from where the current cell can be reached in one step
                prev_positions = self.getPreviousPositions(i, j, N)

                # Add the maximum path which can reach that cell with the current weight of the cell
                distance[i][j] += max(
                    [distance[r][c] for (r, c) in prev_positions]
                )
        
        return max(distance[N-1])


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))
