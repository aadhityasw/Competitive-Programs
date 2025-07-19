class Solution {
	public:

	int lengthOfLongestSubstring(string s) {
		// Get the length of the string
		int n = s.length();

		// There are a total of 256 ascii characters
		// Initialize a vector to store their last occurrence position
		vector<int> lastOccurrance(256, -1);

		// Initialize the sliding window parameters
		// We include indices from (start, end]
		int start = -1;
		int end = -1;

		// Store the maximum length substring (sliding window size) possible
		int maxSubstringLength = 0;

		// Process the string and move the sliding window
		while (end < n-1) {
			// Increase the window
			end++;

			// If the new character is repeated within the window, then shrink the window
			if (lastOccurrance[int(s[end])] > start) {
				start = lastOccurrance[int(s[end])];
			}

            // Update the last occurrance
            lastOccurrance[int(s[end])] = end;

			// Update the max substring length if needed
			maxSubstringLength = max(maxSubstringLength, (end-start));
		}

		return maxSubstringLength;
	}
};
