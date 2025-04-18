// This is for the interview bit version of the problem


int Solution::isMatch(const string A, const string B) {
    // Break the pattern string B into tokens
    vector<string> patternStringTokens;
    for (int i=0; i<B.length(); i++) {
        if (B[i] == '*') {
            continue;
        }
        string curToken="";
        if (i<B.length()-1 && B[i+1] == '*') {
            curToken += B[i];
            curToken += B[i+1];
        }
        else {
            curToken = B[i];
        }
        patternStringTokens.push_back(curToken);
    }

    // Find the number of pattern token and length of A string
    int m = A.length();
    int n = patternStringTokens.size();

    // Initialize a DP grid to process the pattern matching
    vector<vector<bool>> dp(m+1, vector<bool>(n+1, false));

    // Fill the first row, that says match the mattern with null string
    // We fill it to true until we have ".*" pattern that can match empty string
    dp[0][0] = true;
    for (int i=1; i<=n; i++) {
        if (patternStringTokens[i-1].length() < 2) {
            break;
        }
        dp[0][i] = true;
    }

    for (int i=1; i<=m; i++) {
        for (int j=1; j<=n; j++) {
            if (patternStringTokens[j-1].length() == 1) {
                if (patternStringTokens[j-1] == "." || patternStringTokens[j-1][0] == A[i-1]) {
                    dp[i][j] = dp[i-1][j-1];
                }
                else {
                    dp[i][j] = false;
                }
            }
            else if (patternStringTokens[j-1].length() == 2) {
                if (patternStringTokens[j-1][0] == '.' || patternStringTokens[j-1][0] == A[i-1]) {
                    dp[i][j] = dp[i-1][j] || dp[i][j-1];
                }
                else {
                    dp[i][j] = dp[i][j-1];
                }
            }
        }
    }

    // Return the answer
    return dp[m][n]? 1 : 0;
}
