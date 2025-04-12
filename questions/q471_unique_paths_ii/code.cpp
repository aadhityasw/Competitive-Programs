class Solution {
    public:
        int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
            int m = obstacleGrid.size(), n = obstacleGrid[0].size();
            vector<int> dp(n, 0);
            if (obstacleGrid[0][0] == 1) {
                dp[0] = 0;
            }
            else {
                dp[0] = 1;
            }
    
            for (int i=0; i<m; i++) {
                for (int j=0; j<n; j++) {
                    if (obstacleGrid[i][j] == 1) {
                        dp[j] = 0;
                    }
                    else {
                        if (j > 0) {
                            dp[j] += dp[j-1];
                        }
                    }
                }
            }
    
            return dp[n-1];
        }
    };
