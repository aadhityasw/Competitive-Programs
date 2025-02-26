// This is solution to the leetcode version of the problem
// Leetcode Q:36
// The only difference is that the grid is given as characters instead of numbers

#include<vector>
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<int>> vertical(9, vector<int>(9, 0));
        vector<vector<int>> horizontal(9, vector<int>(9, 0));
        vector<vector<int>> regions(9, vector<int>(9, 0));

        for (int i=0; i<9; i++) {
            for (int j=0; j<9; j++) {
                if (board[i][j] == '.') {
                    continue;
                }
                int val = board[i][j] - '0';

                vertical[j][val-1]++;
                if (vertical[j][val-1] > 1) {
                    return false;
                }

                horizontal[i][val-1]++;
                if (horizontal[i][val-1] > 1) {
                    return false;
                }

                int pos = (int(i/3))*3 + int(j/3);
                regions[pos][val-1]++;
                if (regions[pos][val-1] > 1) {
                    return false;
                }
            }
        }

        return true;
    }
};
