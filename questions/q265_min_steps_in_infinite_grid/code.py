class Solution:

    def calculateDistance(self, position1, position2) :
        """
        Given two points, find the distance between them.
        """

        # Destructure the positions of the points
        (x1, y1) = position1
        (x2, y2) = position2

        # Find the difference in the co-ordinates to cover
        diffx = abs(x1 - x2)
        diffy = abs(y1 - y2)

        # Find the path_length
        steps = max(diffx, diffy)

        # Return the distance
        return steps



	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
    def coverPoints(self, A, B):

        # Find the number of points
        n = len(A)

        # Initialize the total path length to 0
        path_length = 0

        # Calculate and store the cumulative path length while traversing through all the paths
        for i in range(n-1) :
            path_length += self.calculateDistance((A[i], B[i]), (A[i+1], B[i+1]))
        
        # Return the total length
        return path_length
