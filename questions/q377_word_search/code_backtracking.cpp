class Solution {
    public:
        bool search(int i, int j, int curPos, vector<vector<char>>& board, vector<vector<bool>>& visited, string word) {
            if (curPos >= word.length()-1) {
                return true;
            }
            
            visited[i][j] = true;
            int possiblePos[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
            int m = board.size(), n = board[0].size();
            for (const auto &inc : possiblePos) {
                int x = i+inc[0];
                int y = j+inc[1];
    
                if (x<0 || y<0 || x>=m || y>=n) {
                    continue;
                }
                if (!visited[x][y] && board[x][y] == word[curPos+1]) {
                    if (search(x, y, curPos+1, board, visited, word)) {
                        return true;
                    }
                }
            }
    
            visited[i][j] = false;
            return false;
        }
    
        bool exist(vector<vector<char>>& board, string word) {
            int m = board.size(), n = board[0].size(), l = word.length();
            vector<vector<bool>> visited(m, vector<bool>(n, false));
            
            for (int i = 0; i<m; i++) {
                for (int j = 0; j<n; j++) {
                    if (board[i][j] == word[0]) {
                        if (search(i, j, 0, board, visited, word)) {
                            return true;
                        }
                    }
                }
            }
    
            return false;
        }
    };
