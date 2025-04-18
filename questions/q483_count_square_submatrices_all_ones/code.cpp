class Solution {
	public:
	int countSquares(vector<vector<int>>& matrix) {
		// Get the size
		int m = matrix.size();
		int n = matrix[0].size();

		// Form a matrix to store the maximum size square that can be formed starting at (i,j)
		vector<vector<int>> squareSize(m, vector<int>(n, 0));
		// Initialize variable to store count of all squares
		int numSquares = 0;

		// Populate the squareSize to find all squares
		for (int i=m-1; i>=0; i--) {
			for (int j=n-1; j>=0; j--) {
				if (matrix[i][j] == 1) {
					int minNeighbor = INT_MAX;
					
					// Check right
					if (j<n-1) {
						minNeighbor = min(minNeighbor, squareSize[i][j+1]);
					}
                    else {
                        minNeighbor = 0;
                    }
					// Check down
					if (i<m-1) {
						minNeighbor = min(minNeighbor, squareSize[i+1][j]);
					}
                    else {
                        minNeighbor = 0;
                    }
					// Check down right diagonal
					if (i<m-1 && j<n-1) {
						minNeighbor = min(minNeighbor, squareSize[i+1][j+1]);
					}
                    else {
                        minNeighbor = 0;
                    }

					squareSize[i][j] = 1 + minNeighbor;

                    // Find sum of all square counts
				    numSquares += squareSize[i][j];
				}
			}
		}

		// Return number of squares found
		return numSquares;
	}
};
