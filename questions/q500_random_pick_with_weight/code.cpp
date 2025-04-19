class Solution {
	public:
	vector<int> prefixSum;
	int totalSum;

	Solution (vector<int>& w) {
		totalSum = 0;
		for (int weight : w) {
			totalSum += weight;
			prefixSum.push_back(totalSum);
		}
	}

	int pickIndex() {
		int randNum = rand() % totalSum;

		// Do a binary search to find the index
		int l = 0, r = prefixSum.size()-1;
		while (l<r) {
			int mid = l + (r-l)/2;
			if (randNum >= prefixSum[mid]) {
				l = mid+1;
			}
			else {
				r = mid;
			}
		}

		return l;
	}
};


/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */
