class Solution {
	public:


	double findDistance(int x1, int y1, int x2, int y2) {
		return double(sqrt(pow(x2-x1,2)+pow(y2-y1,2)));
	}


	vector<vector<int>> formGraph(vector<vector<int>>bombs) {
		// Get the number of bombs
		int n = bombs.size();

		// Initialize the graph
		vector<vector<int>> graph(n);

		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				if (i != j) {
					double dist = findDistance(bombs[i][0], bombs[i][1], bombs[j][0], bombs[j][1]);
					if (dist <= bombs[i][2]) {
						graph[i].push_back(j);
					}
				}
			}
		}

		return graph;
	}


	void searchGraphDFS(int curNode, vector<vector<int>>& graph, vector<bool>& visited, int& numReach) {
		// If the current node is visited, return
		if (visited[curNode]) {
			return;
		}

		// Visit the current node
		visited[curNode] = true;
		numReach++;

		// DFS on the linked nodes
		for (int outEdge : graph[curNode]) {
			searchGraphDFS(outEdge, graph, visited, numReach);
		}
	}


	int maximumDetonation(vector<vector<int>>& bombs) {
		// Form a graph using the bombs
		vector<vector<int>> graph = formGraph(bombs);

		// Store the maximum number of bombs we can detonate
		int maxNumDetonate = 0;

		// From each node do a DFS to see the number of nodes we can reach
		for (int i=0; i<graph.size(); i++) {
			int numReach = 0;
			vector<bool> visited(graph.size(), false);
			searchGraphDFS(i, graph, visited, numReach);

			maxNumDetonate = max(maxNumDetonate, numReach);
		}

		return maxNumDetonate;
	}
};
