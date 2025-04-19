class Solution {
	public:
	int getLargestOutlier(vector<int>& nums) {
		// Get the size
		int n = nums.size();

		// Get a frequency map of every number
		map<int, int> freq;
		for (int num : nums) {
			freq[num]++;
		}

		// Store the largest outlier
		int largestOutlier = INT_MIN;

		// Find the sum of all the numbers
		int total = 0;
		for (int num : nums) {
			total += num;
		}

		// Consider every element as the outlier and then see if you can find (total-cur_ele)/2 in the freq map
		// Because if we remove the outlier, then the remaining sum is just double of the (n-2) element's sum
		for (int i=0; i<n; i++) {
			freq[nums[i]] --;
			if ((total - nums[i])%2 == 0) {
				int eleToFind = (total - nums[i])/2;
				if (freq[eleToFind] > 0) {
					largestOutlier = max(largestOutlier, nums[i]);
				}
			}
freq[nums[i]] ++;	
		}

		return largestOutlier;
	}
};
