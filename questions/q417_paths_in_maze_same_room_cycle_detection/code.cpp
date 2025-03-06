// Uses a set intersection strategy
// Notion is that in order for a cycle of 3 to be formed, we will need one common edge from the two other nodes
// So we just have to count the number of such common nodes from the adjascency list



class Solution {
    public:
        int numberOfPaths(int n, vector<vector<int>>& corridors) {
            vector<set<int>> adj(n+1);
            for (const auto &edge : corridors) {
                adj[edge[0]].insert(edge[1]);
                adj[edge[1]].insert(edge[0]);
            }
    
            int cycleCount = 0;
            for (const auto &edge : corridors) {
                int s = edge[0];
                int d = edge[1];
    
                for (int i : adj[s]) {
                    if (adj[d].count(i) > 0) {
                        cycleCount++;
                    }
                }
            }
    
            return cycleCount / 3;
        }
    };
