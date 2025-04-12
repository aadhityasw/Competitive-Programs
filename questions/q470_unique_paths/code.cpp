class Solution {
    public:
        int uniquePaths(int m, int n) {
            vector<int> dp(n, 0);
            dp[0] = 1;
    
            // Every row of dp at ith iteration would equal the number of possible paths at ith row
            // Make a 2D dp into a 1D dp
            for (int i=0; i<m; i++) {
                for (int j=1; j<n; j++) {
                    dp[j] += dp[j-1];
                }
            }
    
            return dp[n-1];
        }
    };
