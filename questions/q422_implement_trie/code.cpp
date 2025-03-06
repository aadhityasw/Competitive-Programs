class Trie {
    public:
        Trie* children[26];
        bool isTerminal;
    
        Trie() {
            isTerminal = false;
            for (int i=0; i<26; i++) {
                children[i] = nullptr;
            }
        }
        
        void insert(string word) {
            if (word.length() == 0) {
                isTerminal = true;
                return;
            }
    
            if (children[int(word[0])-97] == nullptr) {
                children[int(word[0])-97] = new Trie();
            }
    
            children[int(word[0])-97]->insert(word.substr(1, word.length()-1));
        }
        
        bool search(string word) {
            if (word.length() == 0) {
                if (isTerminal) {
                    return true;
                }
                return false;
            }
    
            if (children[int(word[0]) - 97] == nullptr) {
                return false;
            }
            return children[int(word[0]) - 97]->search(word.substr(1, word.length()-1));
        }
        
        bool startsWith(string prefix) {
            if (prefix.length() == 0) {
                return true;
            }
    
            if (children[int(prefix[0])-97] == nullptr) {
                return false;
            }
            return children[int(prefix[0])-97]->startsWith(prefix.substr(1, prefix.length()-1));
        }
    };
    
    /**
     * Your Trie object will be instantiated and called as such:
     * Trie* obj = new Trie();
     * obj->insert(word);
     * bool param_2 = obj->search(word);
     * bool param_3 = obj->startsWith(prefix);
     */
