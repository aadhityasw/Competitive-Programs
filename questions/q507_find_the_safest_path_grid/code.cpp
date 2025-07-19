class Solution {
	public:


	vector<pair<int, int>> getPositionOfThieves(vector<vector<int>>& grid) {
		// Initialize a vector to store the coordinates
		vector<pair<int, int>> thieves;

		// Get the dimensions of the grid
		int m = grid.size();
		int n = grid[0].size();

		// Find the thieves
		for (int i=0; i<m; i++) {
			for (int j=0; j<n; j++) {
				if (grid[i][j] == 1) {
					thieves.push_back({i, j});
				}
			}
		}

		return thieves;
	}


	vector<vector<int>> calculateDistanceFromThieves(vector<vector<int>>& grid, vector<pair<int, int>> thievesPosition, int& maxDistanceFromThief) {
		// Get the dimensions of the grid
		int m = grid.size();
		int n = grid[0].size();

		// Get the number of thieves
		int numThieves = thievesPosition.size();

		// Initialize grid to store distance to nearest thief
		vector<vector<int>> distToThief(m, vector<int>(n, INT_MAX));

		// Initialize a heap for the multi-source BFS
		priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> frontier;

		// Start a BFS from each thief to update the distances
		for (int i=0; i<numThieves; i++) {
			frontier.push({0, thievesPosition[i].first, thievesPosition[i].second});
		}

		// Store the directional updates
		vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

		// Do the BFS
		while (!frontier.empty()) {
			int x = frontier.top()[1];
			int y = frontier.top()[2];
			int cur_dist = frontier.top()[0];
			frontier.pop();

			// Update the current cell if needed
			if (distToThief[x][y] > cur_dist) {
				distToThief[x][y] = cur_dist;
				maxDistanceFromThief = max(maxDistanceFromThief, cur_dist);

				// Update the neighbors too
				for (auto& dir : directions) {
					int nx = x+dir[0];
					int ny = y+dir[1];

					if (nx>=0 && nx<m && ny>=0 && ny<n && distToThief[nx][ny] > cur_dist+1) {
						frontier.push({cur_dist+1, nx, ny});
					}
				}
			}
		}

        return distToThief;
	}


	bool canReachDestinationWithSafenessLimit(vector<vector<int>>& distToNearestThief, int safenessLimit) {
		// Get the dimensions of the grid
		int m = distToNearestThief.size();
		int n = distToNearestThief[0].size();

		if (distToNearestThief[0][0] < safenessLimit) {
			return false;
		}
		if (distToNearestThief[m-1][n-1] < safenessLimit) {
			return false;
		}

		// Initialize a stack to act as the frontier for the DFS
		stack<pair<int, int>> frontier;
		frontier.push({0, 0});

		// Track the visited cells
		vector<vector<bool>> visited(m, vector<bool>(n, false));

		// Store the directional updates
		vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

		// DO the DFS
		while (!frontier.empty()) {
			int x = frontier.top().first;
			int y = frontier.top().second;
			frontier.pop();

			// If we have reached the destination, return true
			if (x == m-1 && y == n-1) {
				return true;
			}

			if (!visited[x][y]) {
				visited[x][y] = true;

				// Add the neighbors
				for (auto& dir : directions) {
					int nx = x+dir[0];
					int ny = y+dir[1];

					if (nx>=0 && nx<m && ny>=0 && ny<n && !visited[nx][ny] && distToNearestThief[nx][ny] >= safenessLimit) {
						frontier.push({nx, ny});
					} 
				}
			}
		}

		// If we have reached here, then it means we cannot reach the destination with the current safeness limits
		return false;
	}


	int maximumSafenessFactor(vector<vector<int>>& grid) {
		// Get the dimensions of the grid
		int m = grid.size();
		int n = grid[0].size();

		// Get the positions of the thieves
		vector<pair<int, int>> thievesPosition = getPositionOfThieves(grid);

		// Store the maximum distance of any cell to its nearest thief
		int maxDistanceFromThief = INT_MIN;

		// Calculate and store the distance of each cell to the nearest thief
		vector<vector<int>> distToNearestThief = calculateDistanceFromThieves(grid, thievesPosition, maxDistanceFromThief);

		// So the safeness factor can go from 0 till maxDistanceFromThief
		// We need to find the max safeness factor with which we can go from source to destination
		// So we do a binary search on this range
		int high = maxDistanceFromThief;
		int low = 0;
		while (low < high) {
			int mid = low + (high-low)/2;

			// If we can reach dest having the minimum distance to the nearest thief >= mid
			if (canReachDestinationWithSafenessLimit(distToNearestThief, mid)) {
				low = mid+1;
			}
			else {
				high = mid;
			}
		}

		if (!canReachDestinationWithSafenessLimit(distToNearestThief, low)) {
			return low-1;
		}
		return low;
	}
};
