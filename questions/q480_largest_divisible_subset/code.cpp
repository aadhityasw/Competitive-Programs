class Solution {
	public:
	vector<int> largestDivisibleSubset(vector<int>& nums) {
		int n = nums.size();
		// To store the previous index in a chain form
		vector<int> prevIndex(n, -1);
		// To store the length of the largest Divisible subset
		vector<int> dp(n, 1);
		int lengthOfLDS = 1;

		// Sort the array to reduce divisibility check to be in just one direction
		sort(nums.begin(), nums.end());

		// Find the size of the largest divisible subset similar to longest increasing subsequence
		for (int i=0; i<n; i++) {
			for (int j=i+1; j<n; j++) {
				if (nums[j] % nums[i] == 0) {
					if (dp[j] < dp[i]+1) {
						prevIndex[j] = i;
						dp[j] = dp[i]+1;
						lengthOfLDS = max(lengthOfLDS, dp[j]);
					}
				}
			}
		}

		// Initialize a vector to store the LDS
		vector<int> ldsAns;
		// Start from position from back where dp[i] == lengthOfLDS, and use the prevIndex from that pos till prevIndex == -1
		int ind = -1;
		for (int i=n-1; i>=0; i--) {
			if (dp[i] == lengthOfLDS) {
				ind = i;
				break;
			}
		}
		while (ind >= 0) {
			ldsAns.push_back(nums[ind]);
			ind = prevIndex[ind];
		}

		return ldsAns;
	}
};
