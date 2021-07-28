class Solution:

    def getCandidatePositions(self, current_position, matrix) :
        """
        Given the current position in the matrix, returns all the possible next moves that can be placed

        Parameters
        ----------
        current_position - the coordinates of the current position in the matrix
        matrix - the matrix of numbers provided

        Return
        ------
        candidate_positions - a list of all coordinates which can be persued upon from the current cell
        """

        # Decode the coordinates and the dimensions of the matrix
        i, j = current_position
        n, m = len(matrix), len(matrix[0])

        # Movement can be in all four directions
        possible_moves = [
            (i-1, j), (i+1, j),
            (i, j-1), (i, j+1)
        ]

        # Initialize an array to store only the valid moves
        candidate_moves = []

        # Validate all the possible moves, and store the ones which are valid
        for next_i, next_j in possible_moves :
            if 0 <= next_i < n and 0 <= next_j < m and matrix[next_i][next_j] > matrix[i][j] :
                candidate_moves.append((next_i, next_j))
        
        # Return the valid moves
        return candidate_moves


    def dfsSearch(self, current_position, matrix) :
        """
        Performs a Depth First Search through all paths from the current cell.

        Parameters
        ----------
        current_position - the coordinates of the current position in the matrix
        matrix - the matrix of numbers provided

        Return
        ------
        cur_max_distance - the length of the longest increasing subsequence from the current position
        """

        # If this cell has already been processed, we return the saved value from earlier computation
        if current_position in self.store :
            return self.store[current_position]

        # Decode the coordinates of the current cell
        r, c = current_position

        # Initialize a variable to store the maximum of all paths from the current cell
        cur_max_distance = 1

        # Follow through all the paths that are valid
        for next_position in self.getCandidatePositions(current_position, matrix) :
            cur_max_distance = max(
                cur_max_distance,
                1 + self.dfsSearch(next_position, matrix)
            )

        # Store this computed value for performance improvement
        self.store[(r, c)] = cur_max_distance

        # Return this computed value
        return cur_max_distance


    def longestIncreasingPath(self, matrix, n, m):

        # Initialize the maximum distance
        max_distance = float("-inf")

        # Initialze a store for better performance
        self.store = {}

        # Perform DFS from all cells
        for i in range(n) :
            for j in range(m) :
                max_distance = max(
                    max_distance,
                    self.dfsSearch((i, j), matrix)
                )
        
        # Return the maximum distance
        return max_distance




if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[1])]for j in range(n[0])]
        c=0
        for i in range(n[0]):
            for j in range(n[1]):
                matrix[i][j] = arr[c]
                c+=1 
                
        ob = Solution()
        print(ob.longestIncreasingPath(matrix, n[0], n[1]))
