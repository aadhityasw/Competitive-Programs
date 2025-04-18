class Solution {
	public:
	int countSubstrings(string s) {
		// Find the length of the string
		int n = s.length();

		// Initialize a vector to store the count of palindromes that start from index i
		// By default every character in the string is a length=1 palindrome
		vector<int> palindromeCounts(n, 1);

		// Parse through the Indices and find the longer length palindromes
		for (int i=0; i<n; i++) {
			// odd length palindromes
			int left = i-1;
			int right = i+1;
			while (left>=0 && right<n && s[left] == s[right]) {
				// We have a palindrome from s[left:right]
				palindromeCounts[left] ++;
				left--;
				right++;
			}

			// Even length palindromes
			left = i;
			right = i+1;
			while (left>=0 && right<n && s[left] == s[right]) {
				// We have a palindrome from s[left:right]
				palindromeCounts[left] ++;
				left--;
				right++;
			}
		}

		// Find the total number of palindromes
		int totalPalindromeCount = 0;
		for (int curPalindromeCount : palindromeCounts) {
			totalPalindromeCount += curPalindromeCount;
		}

		return totalPalindromeCount;
	}
};
