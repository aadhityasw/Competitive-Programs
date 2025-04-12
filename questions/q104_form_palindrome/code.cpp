// This is for the leetcode version of the problem


class Solution {
    public:
    
        int longestPalindromeSubseq(string s) {
            // Reverse the string s and get its length
            string rev = s;
            reverse(rev.begin(), rev.end());
            int n = s.length();
    
            // Find longest common subsequence length between s and rev
            // Initialize DP grid
            vector<vector<int>> dp(n+1, vector<int>(n+1, 0));
    
            // Fill the DP grid
            for (int i=1; i<=n; i++) {
                for (int j=1; j<=n; j++) {
                    dp[i][j] = dp[i][j-1];
                    dp[i][j] = max( dp[i][j], dp[i-1][j] );
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i-1][j-1] + (s[i-1]==rev[j-1] ? 1 : 0)
                    );
                }
            }
    
            return dp[n][n];
        }
    
        int minInsertions(string s) {
            
            // Find the length of the longest palindromic subsequence
            int palindromeSubseqLength = longestPalindromeSubseq(s);
    
            // Number of edits needed is the total length - number of characters in s that already forms a palindromic subsequence
            // This is because we can add characters anywhere
            return s.length() - palindromeSubseqLength;
        }
    };
