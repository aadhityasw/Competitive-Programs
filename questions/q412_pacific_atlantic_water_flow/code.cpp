class Solution {
    public:
        void search(int i, int j, vector<vector<int>>& heights, vector<vector<bool>>& hasVisited, vector<vector<bool>>& ocean) {
            if (i<0 || i>=heights.size() || j<0 || j>=heights[0].size() || hasVisited[i][j]) {
                return;
            }
    
            hasVisited[i][j] = true;
            ocean[i][j] = true;
            int directions[4][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
    
            for (const auto& dir : directions) {
                if (i+dir[0]>=0 && i+dir[0]<heights.size() && j+dir[1]>=0 && j+dir[1]<heights[0].size()) {
                    if (heights[i+dir[0]][j+dir[1]] >= heights[i][j]) {
                        search(i+dir[0], j+dir[1], heights, hasVisited, ocean);
                    }
                }
            }
        }
    
        vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
            int m = heights.size(), n = heights[0].size();
            vector<vector<bool>> atlantic(m, vector<bool>(n, false));
            vector<vector<bool>> pacific(m, vector<bool>(n, false));
    
            // Can flow to top side to pacific
            vector<vector<bool>> hasVisited(m, vector<bool>(n, false));
            for (int j=0; j<n; j++) {
                search(0, j, heights, hasVisited, pacific);
            }
    
            // Can flow to left side to pacific
            hasVisited.assign(m, vector<bool>(n, false));
            for (int i=0; i<m; i++) {
                search(i, 0, heights, hasVisited, pacific);
            }
    
            // Can flow to bottom side to atlantic
            hasVisited.assign(m, vector<bool>(n, false));
            for (int j=0; j<n; j++) {
                search(m-1, j, heights, hasVisited, atlantic);
            }
    
            // Can flow to right side to atlantic
            hasVisited.assign(m, vector<bool>(n, false));
            for (int i=0; i<m; i++) {
                search(i, n-1, heights, hasVisited, atlantic);
            }
    
            vector<vector<int>> ans;
            for (int i=0; i<m; i++) {
                for (int j=0; j<n; j++) {
                    if (atlantic[i][j] && pacific[i][j]) {
                        ans.push_back({i, j});
                    }
                }
            }
    
            return ans;
        }
    };
