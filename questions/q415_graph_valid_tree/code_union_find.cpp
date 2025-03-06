class Solution {
    public:
        bool validTree(int n, vector<vector<int>>& edges) {
            set<int> visited;
    
            // A graph with n nodes must have exactly n-1 edges for it to not have cycles
            if (edges.size() != n-1) {
                return false;
            }
    
            vector<int> parent(n);
            int numCOmponents = n;
            for (int i=0; i<n; i++) {
                parent[i] = i;
            }
    
            for (const auto &edge : edges) {
                int parentSrc = edge[0];
                while(parent[parentSrc] != parentSrc) {
                    parentSrc = parent[parentSrc];
                }
    
                int parentDest = edge[1];
                while(parent[parentDest] != parentDest) {
                    parentDest = parent[parentDest];
                }
    
                if (parentSrc == parentDest) {
                    // Cycle is present
                    return false;
                }
    
                int minParent = min(parentSrc, parentDest);
                int p = edge[0];
                while (p != minParent) {
                    int temp = parent[p];
                    parent[p] = minParent;
                    p = temp;
                }
    
                p = edge[1];
                while (p != minParent) {
                    int temp = parent[p];
                    parent[p] = minParent;
                    p = temp;
                }
            }
    
            for (int i=0; i<n; i++) {
                int p = i;
                while (parent[p] != p) {
                    int temp = parent[p];
                    parent[p] = parent[parent[p]];
                    p = temp;
                }
            }
    
            for (int i=0; i<n; i++) {
                if (parent[i] != 0) {
                    return false;
                }
            }
    
            return true;
        }
    };
