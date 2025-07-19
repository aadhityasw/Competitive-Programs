class Solution {
	public:

	int kthSmallest(vector<vector<int>>& matrix, int k) {
		// Get the dimension of the square matrix
		int n = matrix.size();

		// Initialize a min heap to store the processed elements
		// Each element is (value, x_coord, y_coord)
		priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> frontier;

		// Initialize a matrix to track elements that are already inside the heap or has already been taken out
		vector<vector<bool>> markedCells(n, vector<bool>(n, false));

		// We start with the (0,0) index and proceed
		frontier.push({matrix[0][0], 0, 0});
		markedCells[0][0] = true;

		// Track the number of elements taken out of the heap
		int numSmallestElementsFound = 0;

		// Proceed with the BFS
		while (!frontier.empty()) {
			// Take out the top element from the stack
			int element = frontier.top()[0];
			int curX = frontier.top()[1];
			int curY = frontier.top()[2];
			frontier.pop();

			// Update the tracker for the smallest elements
			numSmallestElementsFound ++;
			if (numSmallestElementsFound == k) {
				return element;
			}

			// Take the bottom element and insert that into the heap
			if (curX < n-1 && !markedCells[curX+1][curY]) {
				markedCells[curX+1][curY] = true;
				frontier.push({matrix[curX+1][curY], curX+1, curY});
			}

			// Take the right element and insert that into the heap
			if (curY < n-1 && !markedCells[curX][curY+1]) {
				markedCells[curX][curY+1] = true;
				frontier.push({matrix[curX][curY+1], curX, curY+1});
			}
		}

		return -1;
	}
};
