class Solution {
	public:

	int swimInWater(vector<vector<int>>& grid) {
		// Get the dimension of the square grid
		int n = grid.size();

		// Initialize a heap to store the positions to explore
		priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> frontier;
		
		// Initialize a matrix to mark the visited nodes
		vector<vector<bool>> visited(n, vector<bool>(n, false));

		// Add the start position into the heap
		frontier.push({grid[0][0], 0, 0});

		// Proceed with BFS in the grid
		while (!frontier.empty()) {
			// Get the top element
			int curTime = frontier.top()[0];
			int curX = frontier.top()[1];
			int curY = frontier.top()[2];
            frontier.pop();

			// If we have visited a cell before, then it means we were able to reach here before curTime time, so we ignore this instance
			if (visited[curX][curY]) {
				continue;
			}

            // Mark the current cell visited
            visited[curX][curY] = true;

			// If this is the destination cell, then return
			if (curX == n-1 && curY == n-1) {
				return curTime;
			}

			// Proceed with adding the neighboring nodes
			// Add the top node
			if (curX > 0 && !visited[curX-1][curY]) {
				frontier.push({max(grid[curX-1][curY], curTime), curX-1, curY});
			}

			// Add the bottom node
			if (curX < n-1 && !visited[curX+1][curY]) {
				frontier.push({max(grid[curX+1][curY], curTime), curX+1, curY});
			}

			// Add the left node
			if (curY > 0 && !visited[curX][curY-1]) {
				frontier.push({max(grid[curX][curY-1], curTime), curX, curY-1});
			}


			// Add the top node
			if (curY < n-1 && !visited[curX][curY+1]) {
				frontier.push({max(grid[curX][curY+1], curTime), curX, curY+1});
			}
		}

		// If we have reached here, then we were not able to swim to the end
		return -1;
	}
};
