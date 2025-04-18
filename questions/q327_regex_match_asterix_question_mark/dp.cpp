// This is for the leetcode version of the problem


class Solution {
    public:
        bool isMatch(string s, string p) {
            // Get the length of the strings
            int len1 = s.length(), len2 = p.length();
    
            // Form the DP table
            vector<vector<bool>> dp(len1+1, vector<bool>(len2+1, false));
            dp[0][0] = true;
    
            // Fill the first row till there are * as * can match with nothing
            int pos=1;
            while (pos <= len2 && p[pos-1] == '*') {
                dp[0][pos] = true;
                pos++;
            }
    
            for (int i=1; i<=len1; i++) {
                for (int j=1; j<=len2; j++) {
                    if (p[j-1] == '*') {
                        dp[i][j] = dp[i-1][j-1] || dp[i][j-1] || dp[i-1][j];
                    }
                    else if (p[j-1] == '?') {
                        dp[i][j] = dp[i-1][j-1];
                    }
                    else if (p[j-1] == s[i-1]) {
                        dp[i][j] = dp[i-1][j-1];
                    }
                    else {
                        dp[i][j] = false;
                    }
                }
            }
    
            return dp[len1][len2];
        }
    };
