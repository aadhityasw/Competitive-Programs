// Uses the union find strategy

class Solution {
    public:
    
        int getParent(int n, vector<int>& parent) {
            while(n != parent[n]) {
                n = parent[n];
            }
            return n;
        }
    
        void modifyParent(int p, int overallParent, vector<int>& parent) {
            while(p != overallParent) {
                int temp = parent[p];
                parent[p] = overallParent;
                p = temp;
            }
        }
    
        int countComponents(int n, vector<vector<int>>& edges) {
            vector<int> parent(n);
    
            for (int i=0; i<n; i++) {
                parent[i] = i;
            }
    
            for (const auto &edge : edges) {
                int parentSrc = getParent(edge[0], parent);
                int parentDest = getParent(edge[1], parent);
    
                int minParent = min(parentSrc, parentDest);
                modifyParent(parentSrc, minParent, parent);
                modifyParent(parentDest, minParent, parent);
            }
    
            for (int i=0; i<n; i++) {
                int p = getParent(i, parent);
                modifyParent(i, p, parent);
            }
    
            set<int> compParents;
            for (int i=0; i<n; i++) {
                if (compParents.count(parent[i]) == 0) {
                    compParents.insert(parent[i]);
                }
            }
    
            return compParents.size();
        }
    };
