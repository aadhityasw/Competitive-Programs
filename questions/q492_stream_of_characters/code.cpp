class TrieNode {
	public:
	bool isTerminal;
	vector<TrieNode*> children;

	TrieNode () {
		isTerminal = false;
		children.resize(26, nullptr);
	}

	void insert(string word) {
		if (word.length() == 0) {
			isTerminal = true;
            return;
		}

		if (this->children[int(word[0]) - 97] == nullptr) {
			this->children[int(word[0]) - 97] = new TrieNode();
		}
		this->children[int(word[0]) - 97]->insert(word.substr(1));
	}

	bool search(deque<char> queryCache, int pos) {
		if (pos < 0) {
			return this->isTerminal;
		}

        if (this->children[int(queryCache[pos]) - 97] == nullptr) {
            return false;
        }

        if (this->children[int(queryCache[pos]) - 97]->isTerminal) {
            return true;
        }

		return this->children[int(queryCache[pos]) - 97]->search(queryCache, pos-1);
	}
};


class StreamChecker {
	public:

	TrieNode* root;
	int maxLengthWord;
	deque<char> queryCache;


	void processAndStoreWords (TrieNode* root, vector<string>& words) {
		// Find the number of words
		int n = words.size();

		// Insert all the words into the trie in reverse order
		for (string word : words) {
            maxLengthWord = max(maxLengthWord, int(word.length()));

			string revWord = word;
			reverse(revWord.begin(), revWord.end());
			root->insert(revWord);
		}
	}


	bool validateQuerySuffix() {
		// Get the length of the cache
		int n = queryCache.size();

		// Go from the last to front and see if we can end up at any terminal node in the trie
		return root->search(queryCache, n-1);
	}


	StreamChecker(vector<string>& words) {
		maxLengthWord = 0;
		root = new TrieNode();

		// Store the words in the trie and also find the longest word
		processAndStoreWords(root, words);
	}

	bool query (char letter) {
		// Insert the letter into the query cache
		queryCache.push_back(letter);
		
        // The max length of the word is already determined, so we just store the last maxLengthWord characters
        if (queryCache.size() > maxLengthWord) {
			queryCache.pop_front();
		}

		return validateQuerySuffix();
	}
};


/**
 * Your StreamChecker object will be instantiated and called as such:
 * StreamChecker* obj = new StreamChecker(words);
 * bool param_1 = obj->query(letter);
 */
