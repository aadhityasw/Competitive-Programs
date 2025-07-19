class Solution {
	public:

	int networkDelayTime(vector<vector<int>>& times, int n, int k) {
		// Initialize a distance vector
		vector<int> distance(n+1, INT_MAX);
		distance[k] = 0;

		// Relax the edges n-1 times
		for (int i=0; i<n-1; i++) {
			// Go through every edge
			for (int j=0; j<times.size(); j++) {
				// Extract the current edge info
				int src = times[j][0];
				int dest = times[j][1];
				int dur = times[j][2];

				if (distance[src] < INT_MAX && distance[dest] > distance[src]+dur) {
					distance[dest] = distance[src]+dur;
				}
			}
		}

		// Check if we can reach all the nodes and also take the maximum time from this array
		int maxDuration = INT_MIN;
		for (int i=1; i<=n; i++) {
			if (distance[i] == INT_MAX) {
				return -1;
			}
			maxDuration = max(maxDuration, distance[i]);
		}

		return maxDuration;
	}
};
