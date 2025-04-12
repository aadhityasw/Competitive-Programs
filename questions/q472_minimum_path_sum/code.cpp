class Solution {
    public:
        int minPathSum(vector<vector<int>>& grid) {
            int m = grid.size(), n = grid[0].size();
    
            // index 1 to n+1 will be the indices for 0 to n in the grid
            // offestting by 1 for ease
            vector<int> dp(n+1, INT_MAX);
            dp[0] = 0;
            for (int i=0; i<m; i++) {
                for (int j=1; j<n+1; j++) {
                    dp[j] = min(dp[j], dp[j-1]) + grid[i][j-1];
                }
    
                // For further rows, we consider the 0th index as infinity
                dp[0] = INT_MAX;
            }
    
            return dp[n];
        }
    };
