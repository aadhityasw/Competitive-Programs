// O(n^2) and therefore causes TLE
// This is a naive approach where we choose 2 elements and consider one to be sum and if it is, then the other is the outlier 


class Solution {
	public:
	int getLargestOutlier (vector<int>& nums) {
		// Get the value of n (count)
		int n = nums.size();

		// Get the sum of all elements
		int total = 0;
		for (int num : nums) {
			total += num;
		}

		// Initialize a variable to store the largest outlier
		int largestOutlier = INT_MIN;
		
		// Choose a pair of numbers and consider one the sum and the other as the outlier
		// If one is the sum, then the other is an outlier
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				if (i == j) {
					continue;
				}

				// Get the sum of the other n-2 elements
				int specialSum = total - nums[i] - nums[j];

				// Check if any of the choosen numbers are the sum
				if (specialSum == nums[i]) {
					largestOutlier = max(largestOutlier, nums[j]);
				}
				else if (specialSum == nums[j]) {
					largestOutlier = max(largestOutlier, nums[i]);
				}
			}
		}

		return largestOutlier;
	}
};
