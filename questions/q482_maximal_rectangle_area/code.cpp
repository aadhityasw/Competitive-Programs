

class Solution {
	public:
	int maximalRectangle(vector<vector<char>>& matrix) {
		// Find the dimensions
		int m = matrix.size();
		int n = matrix[0].size();

		// Form the matrix to track consecutive 1's row and  column wise
		vector<vector<vector<int>>> consecutiveOnes(m, vector<vector<int>>(n, vector<int>(2, 0)));
		
		for (int i=m-1; i>=0; i--) {
			for (int j=n-1; j>=0; j--) {
				if (matrix[i][j] == '1') {
					// Increase the consecutive ones count in that row
					consecutiveOnes[i][j][0] = 1 + ( j == n-1 ? 0 : consecutiveOnes[i][j+1][0]);
					// Increase the consecutive ones count in that column
					consecutiveOnes[i][j][1] = 1 + ( i == m-1 ? 0 : consecutiveOnes[i+1][j][1]);
				}
			}
		}

		// Find the area of the maximal rectangle
		int maximalRectangleArea = 0;
		for (int i=0; i<m; i++) {
			for (int j=0; j<n; j++) {
				// Single row/column rectangles
				maximalRectangleArea = max(maximalRectangleArea, consecutiveOnes[i][j][0]);
				maximalRectangleArea = max(maximalRectangleArea, consecutiveOnes[i][j][1]);

				// Parse and find the maximum rectangle possible 

                // Check for columns
				int numColumns = consecutiveOnes[i][j][0];
				int numRows = consecutiveOnes[i][j][1];
				for (int k=j; k<j+numColumns; k++) {
					numRows = min(numRows, consecutiveOnes[i][k][1]);
                    // Update the maximal rectangle area
				    maximalRectangleArea = max(maximalRectangleArea, (numRows * (k-j+1)));
				}

				// Check for rows
                numColumns = consecutiveOnes[i][j][0];
				numRows = consecutiveOnes[i][j][1];
				for (int k=i; k<i+numRows; k++) {
					numColumns = min(numColumns, consecutiveOnes[k][j][0]);
                    // Update the maximal rectangle area
				    maximalRectangleArea = max(maximalRectangleArea, ((k-i+1) * numColumns));
				}
			}
		}


		// Return the maximum rectangle's area
		return maximalRectangleArea;
	}
};
