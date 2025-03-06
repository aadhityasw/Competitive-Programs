// This causes time limit exceeded in leetcode, but passes most of the test cases


class Solution {
    public:
        int expand(int i, int j, vector<vector<char>>& matrix) {
            int curSide = 1;
    
            while (i+curSide < matrix.size() && j+curSide<matrix[0].size()) {
                // Down border
                bool shouldExit = false;
                for (int a=j; a<=j+curSide; a++) {
                    if (matrix[i+curSide][a] == '0') {
                        shouldExit = true;
                        break;
                    }
                }
    
                // Right border
                for (int b=i; b<=i+curSide; b++) {
                    if (matrix[b][j+curSide] == '0') {
                        shouldExit = true;
                        break;
                    }
                }
    
                if (shouldExit) {
                    break;
                }
                curSide++;
            }
    
            return curSide;
        }
    
        int maximalSquare(vector<vector<char>>& matrix) {
            int m = matrix.size(), n = matrix[0].size();
            int maxSide=0;
    
            for (int i=0; i<m; i++) {
                for (int j=0; j<n; j++) {
                    if (matrix[i][j] == '1') {
                        maxSide = max(maxSide, expand(i, j, matrix));
                    }
                }
            }
    
            return maxSide*maxSide;
        }
    };
