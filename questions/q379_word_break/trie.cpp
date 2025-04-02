// This is for the leetcode version of the problem


class TrieNode {
	public:
	bool  isTerminal;
	vector<TrieNode*> children;

	TrieNode() {
		isTerminal = false;
		children.resize(26);
	}
};



class Solution {
	public:
	bool wordBreak(string s, vector<string>& wordDict) {
		
		// Construct trie structure from the word dictionary
		TrieNode* root = constructTrie(wordDict);

		vector<bool> seen(s.length()+1, false);
		stack<int> frontier;
		frontier.push(-1);

		// Do the DFS
		while (!frontier.empty()) {
			int pos = frontier.top() + 1;
            frontier.pop();
			seen[pos] = true;
			if (pos == s.length()) {
				return true;
			}

			// Search through the trie structure
			TrieNode* ptr = root;
			while (ptr != nullptr && pos < s.length() && ptr->children[int(s[pos])-97] != nullptr) {
				ptr = ptr->children[int(s[pos])-97];
				if (ptr->isTerminal && !seen[pos+1]) {
					frontier.push(pos);
				}
				pos++;
			}
		}

		return false;
	}




	TrieNode* constructTrie(vector<string>& wordDict) {
		TrieNode* root = new TrieNode();

		for (string word : wordDict) {
			TrieNode* ptr = root;
			for (char c : word) {
				if (ptr->children[int(c)-97] == nullptr) {
					ptr->children[int(c)-97] = new TrieNode();
				}
				ptr = ptr->children[int(c)-97];
			}
			ptr->isTerminal = true;
		}
		
		return root;
	}
};
