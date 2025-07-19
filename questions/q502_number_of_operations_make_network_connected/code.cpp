class Solution {
	public:

	int findParent(int node, vector<int>& parents) {
		// Recursively search through the parents vector to find the source vector of this connected components
		int ptr = node;
		while (parents[ptr] != ptr) {
			ptr = parents[ptr];
		}
		return ptr;
	}


	void changeParentWithValue(int node, int updateParentVal, vector<int>& parents) {
		int ptr = node;

		while (updateParentVal != parents[ptr]) {
			int temp = parents[ptr];
			parents[ptr] = updateParentVal;
			ptr = temp;
		}
	}


	void mergeComponents(int nodeA, int nodeB, vector<int>& parents) {
		// Find the parents of the nodes
		int parentA = findParent(nodeA, parents);
		int parentB = findParent(nodeB, parents);

		// If they belong to the same component, just return
		if (parentA == parentB) {
			return;
		}

		// Else update both the components with the minParent
		if (parentA < parentB) {
			changeParentWithValue(nodeB, parentA, parents);
		}
		else {
			changeParentWithValue(nodeA, parentB, parents);
		}
	}


	void updateParent(int node, vector<int>& parents) {
		// Find the overall parent of the node
		int overallParent = findParent(node, parents);

		// Update throughout the chain
		changeParentWithValue(node, overallParent, parents);
	}


	int makeConnected(int n, vector<vector<int>>& connections) {
		// Get the number of connections available
		int numConnectionsAvailable = connections.size();

		// Initialize a vector to store the parents
		vector<int> parents(n);
		for (int i=0; i<n; i++) {
			parents[i] = i;
		}

		// Store the number of extra wires
		int numExtraConnectionsAvailable = 0;

		// With every connections, we implement the union find algorithm and modify the parents of the nodes
		// If for a connection, both the vertices belong to the same component, then we just increment the number of extra connections
		for (int i=0; i<numConnectionsAvailable; i++) {
			int nodeA = connections[i][0];
			int nodeB = connections[i][1];

			// Find their parents
			int parentA = findParent(nodeA, parents);
			int parentB = findParent(nodeB, parents);

			if (parentA == parentB) {
				// If the parents are the same, we just increment the number of extra connections
				numExtraConnectionsAvailable ++;
			}
			else {
				// If they have different parents, then merge the components
				mergeComponents(nodeA, nodeB, parents);
			}
		}

		// Loop through all the nodes and make sure the parents of the same connected components have the same value
		for (int i=0; i<n; i++) {
			updateParent(i, parents);
		}

		// After the Union Find Algorithm, find the number of different connected components
		int numConnectedComponents = 0;
		set<int> connectedComponents;
		for (int i=0; i<n; i++) {
			if (connectedComponents.count(parents[i]) == 0) {
				connectedComponents.insert(parents[i]);
				numConnectedComponents ++;
			}
		}

		// Now figure out if we can connect all the computers
		if (numExtraConnectionsAvailable >= (numConnectedComponents-1)) {
			return numConnectedComponents - 1;
		}
		else {
			return -1;
		}
	}
};
