class Solution {
    public:
        int numVisited;
        bool hasCycle;
    
        void search(int curNode, int prevNode, set<int>& visitedNodes, vector<set<int>>& adj) {
            if (prevNode!= -1 && visitedNodes.count(curNode) > 0) {
                hasCycle = true;
                return;
            }
    
            visitedNodes.insert(curNode);
            numVisited++;
            for (int n : adj[curNode]) {
                if (n!= prevNode && !hasCycle) {
                    search(n, curNode, visitedNodes, adj);
                }
            }
        }
    
        bool validTree(int n, vector<vector<int>>& edges) {
            vector<set<int>> adj(n);
            set<int> visited;
    
            for (const auto &ele : edges) {
                adj[ele[0]].insert(ele[1]);
                adj[ele[1]].insert(ele[0]);
            }
    
            hasCycle = false;
            search(0, -1, visited, adj);
            return numVisited == n && !hasCycle;
        }
    };
