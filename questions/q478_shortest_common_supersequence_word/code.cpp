class Solution {
	public:
	string shortestCommonSupersequence(string str1, string str2) {
		// Find the length of the strings
		int l1 = str1.length();
		int l2 = str2.length();

		// Find the longest common subsequence
		vector<vector<int>> dp(l1+1, vector<int>(l2+1, 0));

		for (int i=1; i<=l1; i++) {
			for (int j=1; j<=l2; j++) {
				dp[i][j] = max(dp[i-1][j], dp[i][j-1]);

				dp[i][j] = max(
					dp[i][j],
					dp[i-1][j-1] + (str1[i-1] == str2[j-1] ? 1 : 0)
				);
			}
		}

		// Parse from the bottom right to the top left to get the supersequence
		string supersequence = "";
		int i = l1, j = l2;
		while (i>0 || j>0) {
			// If the character is equal, then it was a part of the subsequence
			if (i>0 && j>0 && str1[i-1] == str2[j-1]) {
				supersequence.push_back(str1[i-1]);

				// Move diagonally up
				i --;
				j--;
			}

			// If characters are not equal, move left / top depending on which is greater
			else if ((i>0 && j>0 && dp[i-1][j] >= dp[i][j-1]) || j == 0) {
				// Move top
				supersequence.push_back(str1[i-1]);
				i--;
			}
			else if ((i>0 && j>0 && dp[i-1][j] < dp[i][j-1]) || i == 0) {
				// Move left
				supersequence.push_back(str2[j-1]);
				j--;
			}
		}

		// Reverse the supersequence string
		reverse(supersequence.begin(), supersequence.end());

		return supersequence;
	}
};
