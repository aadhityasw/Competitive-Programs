// This is for the leetcode version of the problem

class Solution {
	public:
	int lengthOfLIS(vector<int>& nums) {
		// Get the size
		int n = nums.size();

		// Form the DP matrix
		vector<int> dp(n, 1);

        // For every element before ith index that is less than nums[i], we add 1 to its length and maintain the max;
		for (int i=1; i<n; i++) {
			for (int j=0; j<i; j++) {
				if (nums[j] < nums[i]) {
					dp[i] = max(dp[i], 1+dp[j]);
				}
			}
		}

		int maxLen = 0;
		for (int i=0; i<n; i++) {
			maxLen = max(maxLen, dp[i]);
		}

		return maxLen;
	}
};
