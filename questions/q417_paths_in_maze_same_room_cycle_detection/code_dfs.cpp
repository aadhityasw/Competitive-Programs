// Causes Time limit exceeded, but passes most of the test cases

class Solution {
    public:
        set<vector<int>> cycles;
    
        void startSearch(int p, vector<int>& path, set<int>& pathSet, vector<vector<int>>& adj) {
            if (pathSet.count(p) > 0) {
                if (path.size() >= 3) {
                    if (path[path.size()-3] == p) {
                        int n = path.size();
                        vector<int> curCycle = {path[n-3], path[n-2], path[n-1]};
                        sort(curCycle.begin(), curCycle.end());
                        cycles.insert(curCycle);
                    }
                }
                return;
            }
    
            path.push_back(p);
            pathSet.insert(p);
    
            for (int outEdge : adj[p]) {
                startSearch(outEdge, path, pathSet, adj);
            }
    
            path.pop_back();
            pathSet.erase(p);
        }
    
        int numberOfPaths(int n, vector<vector<int>>& corridors) {
    
            vector<vector<int>> adj(n);
            for (const auto &edge : corridors) {
                adj[edge[0]-1].push_back(edge[1]-1);
                adj[edge[1]-1].push_back(edge[0]-1);
            }
    
            for (int i=0; i<n; i++) {
                vector<int> path;
                set<int> pathSet;
    
                startSearch(i, path, pathSet, adj);
            }
    
            return cycles.size();
        }
    };
