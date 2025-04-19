class Solution {
	public:

	bool canMakeAllZerosAfterKQueries(vector<int>& nums, vector<vector<int>>& queries, int k) {
		// If the number of queries to choose is too much, then we just return
		if (k > queries.size()) {
			return false;
		}

		// Get the size of the nums array
		int arraySize = nums.size();

		// Get the number of queries
		int numQueries = k;

		// Create a diff array of size 1+arraySize (In case the query extends till the end of the array
		vector<int> diffArray(arraySize+1, 0);

		// For each query mark the start and end of the query in the diffArray
		// Start is marked with -1 saying we will have to decrease from here
		// End is marked with 1 saying that query has ended so we dont have to do the -1 thing for that particular query
		for (int i=0; i<numQueries; i++) {
			diffArray[queries[i][0]] -= queries[i][2];
			diffArray[queries[i][1]+1] += queries[i][2];
		}

		// Find the overall diff array by doing a prefix sum logic
		for (int i=1; i<arraySize; i++) {
			diffArray[i] += diffArray[i-1];
		}

		// Figure out if all the cells of the array can be made 0
		bool canMakeAllZeros = true;
		for (int i=0; i<arraySize; i++) {
			if (nums[i] + diffArray[i] > 0) {
				canMakeAllZeros = false;
				break;
			}
		}

		return canMakeAllZeros;
	}


	int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
		// Get the size of nums
		int arraySize = nums.size();

        // Check if nums is already all zeros
        bool isAllZeros = true;
        for (int num : nums) {
            if (num > 0) {
                isAllZeros = false;
                break;
            }
        }
        if (isAllZeros) {
            return 0;
        }

		// Get the number of queries
		int numQueries = queries.size();

		// Do a binary search from 0 to numQueries and at every step apply first k queries and check
		int lowK = 0;
		int highK = numQueries-1;
		while (lowK < highK) {
			int curK = lowK + (highK - lowK)/2;

			if (!canMakeAllZerosAfterKQueries(nums, queries, curK+1)) {
				lowK = curK + 1;
			}
			else {
				highK = curK;
			}
		}

		if (lowK >= numQueries || !canMakeAllZerosAfterKQueries(nums, queries, lowK+1)) {
			// Even if all the queries cant make this nums array all zeros
			return -1;
		}
		return lowK+1;
	}
};
