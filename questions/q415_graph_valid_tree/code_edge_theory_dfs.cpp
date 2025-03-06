class Solution {
    public:
        bool validTree(int n, vector<vector<int>>& edges) {
            set<int> visited;
    
            // A graph with n nodes must have exactly n-1 edges for it to not have cycles
            if (edges.size() != n-1) {
                return false;
            }
    
            vector<set<int>> adj(n);
            for (const auto &edge : edges) {
                adj[edge[0]].insert(edge[1]);
                adj[edge[1]].insert(edge[0]);
            }
    
            // A graph must be fully connected too
            int numVisited = 0;
            stack<vector<int>> frontier;
            frontier.push({0, -1});
    
            while (frontier.size() > 0) {
                vector<int> curNode = frontier.top();
                frontier.pop();
                int curNum = curNode[0], prevNum = curNode[1];
                if (visited.count(curNum) > 0) {
                    return false;
                }
                visited.insert(curNum);
                numVisited++;
                for (int nextNum : adj[curNum]) {
                    if (nextNum != prevNum) {
                        frontier.push({nextNum, curNum});
                    }
                }
            }
    
            return numVisited == n;
        }
    };
