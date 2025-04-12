class Solution {
    public:
        int numDistinct(string s, string t) {
            
            // Find the length of the strings
            int sLen = s.length(), tLen = t.length();
    
            // Form the DP table
            // If s[i] == t[j], then take from top and diagonal and add them
            // Else,  take the top
            // In the DP table - X axis - t string, Y axis - s string
            // dp[i][j] = number of distinct subsequences of t[:j] in s[:i]
            // We initialize first column as 1, because we can have 1 distinct subsequence of choosing nothing from nothing
    
            vector<vector<double>> dp(sLen+1, vector<double>(tLen+1, 0));
            dp[0][0] = 1;
    
            for (int i=1; i<=sLen; i++) {
                dp[i][0] = 1;
                for (int j=1; j<=tLen; j++) {
                    if (s[i-1] == t[j-1]) {
                        dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
                    }
                    else {
                        dp[i][j] = dp[i-1][j];
                    }
                }
            }
    
            return (int)dp[sLen][tLen];
        }
    };
