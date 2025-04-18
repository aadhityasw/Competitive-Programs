// This can be reduced to 1D DP as we only depend on top and left element for updating the current cell in the DP table

class Solution {
	public:

	bool isInterleave(string s1, string s2, string s3) {
		// Get the length of the strings
		int l1 = s1.length();
		int l2 = s2.length();
		int l3 = s3.length();

		// Check for basic conditions to fulfil
		if (l1+l2 != l3) {
			// Sum of s1 and s2's length does not match s3's length
			return false;
		}

		// Create a matrix to store the dp values
		// Value at (i,j) denotes if we can form s3[:i+j] using s1[:i] and s2[:i]
		vector<vector<bool>> dp(l1+1, vector<bool>(l2+1, false));

		// We can form s3[:0] from s1[:0] and s2[:0]
		dp[0][0] = true;

		// Fill the first row, taking nothing from s1 and only from s2
		for (int i=1; i<=l2; i++) {
			if (s2[i-1] != s3[i-1]) {
				break;
			}
			dp[0][i] = true;
		}

		// Fill the first column, taking nothing from s2 and only from s1 
		for (int i=1; i<=l1; i++) {
			if (s1[i-1] != s3[i-1]) {
				break;
			}
			dp[i][0] = true;
		}

		// Recursive conditions (Step)
		// Fill the rest of the DP table
		for (int i=1; i<=l1; i++) {
			for (int j=1; j<=l2; j++) {
				dp[i][j] = (
					// We take the s2[j]'th element as next in s3
					dp[i][j-1] && s2[j-1] == s3[i+j-1]
				) || (
					// We take the s1[i]'th element as next in s3
					dp[i-1][j] && s1[i-1] == s3[i+j-1]
				);
			}
		}

		// Return the final answer
		return dp[l1][l2];
	}
};
