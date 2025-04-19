class Solution {
	public:
	bool isZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
		// Get the size of the nums array
		int arraySize = nums.size();

		// Get the number of queries
		int numQueries = queries.size();

		// Create a diff array of size 1+arraySize (In case the query extends till the end of the array
		vector<int> diffArray(arraySize+1, 0);

		// For each query mark the start and end of the query in the diffArray
		// Start is marked with -1 saying we will have to decrease from here
		// End is marked with 1 saying that query has ended so we dont have to do the -1 thing for that particular query
		for (int i=0; i<numQueries; i++) {
			diffArray[queries[i][0]] --;
			diffArray[queries[i][1]+1] ++;
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
};
