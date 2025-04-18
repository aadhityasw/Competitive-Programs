// This is the solution for the leetcode version


class Solution {
    public:
        int minDistance(string word1, string word2) {
            // DIrectional Info
            // Left to right - add a character
            // top to bottom - delete a character
            // Diagonal right down - replace a character if not equal
    
            // Form a DP table
            int len1 = word1.length(), len2 = word2.length();
            vector<vector<int>> dp(len1+1, vector<int>(len2+1, 0));
    
            // Fill the first row
            for (int i=1; i<=len2; i++) {
                dp[0][i] = dp[0][i-1] + 1;
            }
            for (int i=1; i<=len1; i++) {
                dp[i][0] = dp[i-1][0] + 1;
                for (int j=1; j<=len2; j++) {
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1;
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i-1][j-1] + (word1[i-1] == word2[j-1] ? 0 : 1)
                    );
                }
            }
    
            return dp[len1][len2];
        }
    };
