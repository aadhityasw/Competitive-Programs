class Solution {
	public:
	int cutRod(vector<int>& price) {
		int n = price.size();

		vector<int> dp(n+1, 0);

		// Fill the DP table
		// i - rod lengths
		// j - total length of rod till now
		for (int i=1; i<=n; i++) {
			for (int j=1; j<=n; j++) {
				if (j >= i) {
					dp[j] = max(
						dp[j],      // Do not include an i- size rod
						dp[j-i] + price[i-1]    // Choose to include i size rod
					);
				}
			}
		}

        // We need answer for a rod of length n
		return dp[n];
	}
};
