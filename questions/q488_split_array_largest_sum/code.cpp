class Solution {
	public:

	int formGroupsWithLimit(vector<int>& nums, int limit) {
		// Initialize a variable to track the number of groups
		int numGroups=0;

		// Maintain a running sum that resets to 0 if we go over limit
		int runningSum = 0;

		for (int num : nums) {
			// If a single number is larger than limit, then we cannot form groups, so we return inf to increase the limit
			if (num > limit) {
				return INT_MAX;
			}

			// Increase the number of groups if we go over the limit
			if (runningSum + num > limit) {
				runningSum = num;
				numGroups++;
			}
            else {
                runningSum += num;
            }
		}

		// Include the last group
		if (runningSum > 0) {
			numGroups++;
		}

		// Return the number of groups that can be formed
		return numGroups;
	}

	int splitArray(vector<int>& nums, int k) {
		// Find the total sum of all the numbers
		int total = 0;
		for (int num : nums) {
			total += num;
		}

		// We will do a binary search to find the ideal candidate
		// Initialize the search space
		int low = 0;
		int high = total;

		// Do the binary search
		while (low < high) {
			int mid = low + (high-low)/2;
			
			// See the number of groups we can form with mid as the limit for each group
			int numGroups = formGroupsWithLimit(nums, mid);

			// If we can form more than k groups, we need to look in the upper half
			if (numGroups > k) {
				low = mid + 1;
			}
			else {
				high = mid;
			}
		}

		// The final value of low will be our answer
		return low;
	}
};
