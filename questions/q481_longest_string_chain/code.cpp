class Solution {
	public:

	static bool wordComparator(const string& a, const string& b) {
		if (a.length() < b.length()) {
			return true;
		}
        return false;
	}

	bool isPredecessor(string a, string b) {
		// B string should be exactly 1 longer than A string, as we can make only one character addition
		if (b.length() - a.length() != 1) {
			return false;
		}

		int numCharDiff = 0;
		int p1=0, p2=0;
		while (p1 < a.length()) {
			if (a[p1] != b[p2]) {
				numCharDiff ++;

				if (numCharDiff > 1) {
					return false;
				}
				if (a[p1] != b[p2+1]) {
					return false;
				}
				else {
					p2++;
				}
			}
			p1++;
			p2++;
		}

		return true;
	}

	int longestStrChain(vector<string>& words) {
        // Sort the strings
		sort(words.begin(), words.end(), wordComparator);

		// Get the number of words
		int n = words.size();

		// Initialize vectors for storing the longest chain length till ith index and also the prev_index of the chain
		// By default every word is a part of word chain of length 1
		vector<int> dp(n, 1);
		// Get the length of the longest chain
		int longestChainLength = 1;

        // Preprocess the words and store the indices according to length
        map<int, vector<int>> wordLengthToInd;
        for (int i=0; i<n; i++) {
            wordLengthToInd[words[i].length()].push_back(i);
        }

		// Use the Longest Increasing subsequence strategy to fill the dp arrays
		for (int i=0; i<n; i++) {
			for (int j : wordLengthToInd[words[i].length()+1]) {				
				if (isPredecessor(words[i], words[j])) {
					if (dp[j] < dp[i]+1) {
						dp[j] = dp[i]+1;
						longestChainLength = max(longestChainLength, dp[j]);
					}
				}
			}
		}

		return longestChainLength;
	}
};
