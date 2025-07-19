class Solution {
public:

    vector<vector<int>> formGraphFromEdges(vector<vector<int>>& edges) {
        int n = edges.size()+1;
        vector<vector<int>> graph(n);
        for (int i=0; i<edges.size(); i++) {
            graph[edges[i][0]].push_back(edges[i][1]);
            graph[edges[i][1]].push_back(edges[i][0]);
        }
        return graph;
    }

    void startBFSFromNode(int node, vector<vector<int>>& graph, vector<vector<int>>& reachabilityMatrix, int k) {

        // Create a queue to act as the froniter
        queue<vector<int>> frontier;
        frontier.push({node, 0});

        int n = graph.size();
        vector<bool> visited(n, false);

        int curInd = -1;
        int curCount = 0;
        while (!frontier.empty() && frontier.front()[1] <= k) {
            int curNode = frontier.front()[0];
            int curNodeInd = frontier.front()[1];
            visited[curNode] = true;
            frontier.pop();
            

            if (curInd < curNodeInd) {
                if (curInd >= 0) {
                    reachabilityMatrix[curInd][node] = curCount;
                }
                curInd = curNodeInd;
            }
            curCount++;

            for (int nextNode : graph[curNode]) {
                if (!visited[nextNode] && curNodeInd < k) {
                    frontier.push({nextNode, curNodeInd+1});
                }
            }
        }
        for (int i=curInd; i<=k; i++) {
            reachabilityMatrix[i][node] = curCount;
        }
    }

    vector<vector<int>> formRechabilityMatrix(vector<vector<int>>& graph, int k) {
        int n = graph.size();
        vector<vector<int>> reachabilityMatrix (k+1, vector<int>(n, 1));

        // Do a BFS from every node to populate this matrix
        for (int i=0; i<n; i++) {
            startBFSFromNode(i, graph, reachabilityMatrix, k);
        }
        
        return reachabilityMatrix;
    }

    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2, int k) {
        
        // Form the Graphs from the edges
        vector<vector<int>> graph1 = formGraphFromEdges(edges1);
        vector<vector<int>> graph2 = formGraphFromEdges(edges2);

        // Preprocess the graphs to form the rechability matrix
        // dimension = (k+1, edges.size()+1)
        vector<vector<int>> rechabilityMatrix1 = formRechabilityMatrix(graph1, k);
        vector<vector<int>> rechabilityMatrix2 = formRechabilityMatrix(graph2, k);

        // Find the answers for all the queries
        vector<int> answers (edges1.size()+1, 1);
        if (k > 0) {
            for (int i=0; i<=edges1.size(); i++) {
                int cross_tree_count = 0;
                for (int j=0; j<=edges2.size(); j++) {
                    cross_tree_count = max(cross_tree_count, rechabilityMatrix2[k-1][j]);
                }
                // Sum of in-tree search  +  cross-tree search
                answers[i] = rechabilityMatrix1[k][i] + cross_tree_count;
            }
        }

        return answers;
    }
};
