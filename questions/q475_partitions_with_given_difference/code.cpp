// Login behind this is
// s1 and s2 are the sum of the subsets
// s1 + s2 = tSum
// s1 - s2 = d


class Solution {
	public:
	int countPartitions(vector<int>& arr, int d) {
		int n = arr.size();
		
		// Find the total sum
		int totalSum = 0;
		for (int num : arr) {
		    totalSum += num;
		}
		
		// Find the target
		int target = (totalSum - d) / 2;
		if ((totalSum - d) % 2 == 1 || (totalSum - d) < 0) {
		    return 0;
		}

		// Form a DP array
		vector<vector<int>> dp(n+1, vector<int>(target+1, 0));
		dp[0][0] = 1;

		// DP loop
		for (int i=1; i<=n; i++) {
			for (int j=0; j<=target; j++) {
				dp[i][j] = dp[i-1][j];
				if (arr[i-1] <= j) {
					dp[i][j] += dp[i-1][j - arr[i-1]];
				}
			}
		}

		return dp[n][target];
	}
};
