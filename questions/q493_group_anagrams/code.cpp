class Solution {
	public:

	vector<int> encodeWord(string word) {
		vector<int> code(26, 0);
		for (char c : word) {
			code[int(c) - 97] ++;
		}

		return code;
	}

	vector<vector<string>> groupAnagrams(vector<string>& strs) {
		// Find the number of words
		int n = strs.size();

		// Declare a map to store the encoded version of the string and map it to all occurances of the words
		// Words with same letter combinations in the same count will have the same encoded version
		map<vector<int>, vector<string>> codeToStrings;

		// Encode and store the words in the map
		for (string word : strs) {
			vector<int> curEncodedWord = encodeWord(word);
			codeToStrings[curEncodedWord].push_back(word);
		}

		// Initialize a vector to store the results
		vector<vector<string>> result;
		for (const auto &pair : codeToStrings) {
			result.push_back(pair.second);
		}
		return result;
	};
};
