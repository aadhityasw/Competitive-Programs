class Trie {
    public:
    Trie *children[26];
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
        if (children[word[0] - 'a'] == nullptr) {
            children[word[0] - 'a'] = new Trie();
        }
        children[word[0] - 'a']->insert(word.substr(1, word.length()-1));
    }
};

class Solution {
public:
    set<string> ans;

    void search(int i, int j, Trie* ptr, vector<vector<char>>& board, vector<vector<bool>>& visited, string curPath) {
        if (ptr == nullptr) {
            return;
        }
        if (ptr->isTerminal) {
            ans.insert(curPath);
        }

        int m=board.size(), n=board[0].size();
        visited[i][j] = true;
        int possiblePaths[4][2] = {{-1,0}, {1,0}, {0,-1}, {0,1}};
        for (const auto &path : possiblePaths) {
            int x = i+path[0];
            int y = j+path[1];
            if (x<0 || y<0 || x>=m || y>=n) {
                continue;
            }

            if (!visited[x][y] && ptr->children[board[x][y] - 'a'] != nullptr) {
                search(x, y, ptr->children[board[x][y] - 'a'], board, visited, curPath+board[x][y]);
            }
        }
        visited[i][j] = false;
    }

    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        Trie *root = new Trie();

        for (string word : words) {
            root->insert(word);
        }

        int m=board.size(), n=board[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (root->children[board[i][j] - 'a'] != nullptr) {
                    string curPath(1, board[i][j]);
                    search(i, j, root->children[board[i][j] - 'a'], board, visited, curPath);
                }
            }
        }

        vector<string> ans2(ans.begin(), ans.end());
        return ans2;
    }
};
