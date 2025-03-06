class Solution {
    public:
        void markIslandVisited(int i, int j, vector<vector<char>>& grid, vector<vector<bool>>& hasVisited) {
            int m = grid.size(), n = grid[0].size();
    
            if (i<0 || i>=m || j<0 || j>=n || hasVisited[i][j]) {
                return;
            }
            if (grid[i][j] == '0') {
                return;
            }
    
            hasVisited[i][j] = true;
            int neighbors[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0,-1}};
    
            for (const auto& k : neighbors) {
                markIslandVisited(i+k[0], j+k[1], grid, hasVisited);
            }
        }
    
        int numIslands(vector<vector<char>>& grid) {
            int m = grid.size(), n = grid[0].size();
            vector<vector<bool>> hasVisited(m, vector<bool>(n, false));
    
            int numIslands = 0;
            for (int i=0; i<m; i++) {
                for (int j = 0; j<n; j++) {
                    if (grid[i][j] == '1' && !hasVisited[i][j]) {
                        numIslands++;
                        markIslandVisited(i, j, grid, hasVisited);
                    }
                }
            }
    
            return numIslands;
        }
    };
