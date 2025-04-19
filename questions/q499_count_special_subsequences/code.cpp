class Solution {
	public:

	int searchInArray(vector<int>& positions, int searchIndex) {
		// Get the size of the array
		int n = positions.size();

        if (n == 0) {
            return 0;
        }

		// Initialize parameters for the search
		// This is a sorted array, so do binary search
		int low = 0;
		int high = n-1;
		while (low < high) {
			int mid = low + (high-low)/2;
			if (searchIndex < positions[mid]) {
				high = mid;
			}
			else {
				low = mid+1;
			}
		}

		if (low < positions.size() && positions[low] > searchIndex) {
			return low;
		}
		return low+1;
	}

	long long numberOfSubsequences(vector<int>& nums) {
		// Get the size of nums
		int n = nums.size();

		// The dict maps the p/q value to indices of q that form this p/q 
		map<double, vector<int>> dividedToPositions;

		// Pre-process the array
		// Get all possible values of p/q from the array
		for(int i=0; i<n; i++) {
			for (int j=i+2; j<n; j++) {
				dividedToPositions[(double)nums[i]/nums[j]].push_back(j);
			}
		}

		// Sort all the position arrays in the map
		for (const auto& pair : dividedToPositions) {
			sort(dividedToPositions[pair.first].begin(), dividedToPositions[pair.first].end());
		}

		// To store the final answer
		long long numSubsequences = 0;

		// Loop through the values and consider that as position r
		for (int r = 4; r < n-2; r++) {
			// Take the value of s
			for (int s = r+2; s < n; s++) {
				double rhs = (double)nums[s] / nums[r];
				int maxQPos = r-2;

				// Use binary search and find number of possible p/q values from the map before the maxQPos index
				numSubsequences += searchInArray(dividedToPositions[rhs], maxQPos);
			}
		}

		return numSubsequences;
	}
};
