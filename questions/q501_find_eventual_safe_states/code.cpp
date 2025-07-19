class Solution {
	public:

	vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
		// Get the total number of nodes
		int V = graph.size();

		// Form an inverted graph that maps a vertex to incoming edges
		vector<vector<int>> invertedGraph(V);

		for (int inEdge=0; inEdge<V; inEdge++) {
			for (int outEdge : graph[inEdge]) {
				invertedGraph[outEdge].push_back(inEdge);
			}
		}

		// Copy the graph to an adjacency set form for better access
		vector<set<int>> graphSet(V);
		for (int i=0; i<V; i++) {
			for (int outNode : graph[i]) {
				graphSet[i].insert(outNode);
			}
		}

		// Do a topological sorted order as much as possible
		// This would be the list of safe nodes
		
		// Initialize a frontier of terminal nodes
		queue<int> frontier;

		for (int i=0; i<V; i++) {
			if (graph[i].size() == 0) {
				frontier.push(i);
			}
		}

		// Maintain whether a node is safe or not
		vector<int> isSafeNode(V, false);

		// Topological Sort
		while (!frontier.empty()) {
			int curNode = frontier.front();
			frontier.pop();

			isSafeNode[curNode] = true;

			// Remove the incoming edges to the node
			for (int inNode : invertedGraph[curNode]) {
				graphSet[inNode].erase(curNode);
				if (graphSet[inNode].size() == 0) {
					// If there are no more outgoing edges, then add it to the frontier
					frontier.push(inNode);
				}
			}
		}

		// Accumulate the safe nodes
		vector<int> safeNodes;
		for (int i=0; i<V; i++) {
			if (isSafeNode[i]) {
				safeNodes.push_back(i);
			}
		}

		return safeNodes;
	}
};
