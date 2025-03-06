// Approach similar to a bottom up DP, construct a DP table
// Look at the left, top and top left diagonal element and decide if the size of the matrix should increase or not at every step

class Solution {
    public:
        int maximalSquare(vector<vector<char>>& matrix) {
            int m = matrix.size();
            int n = matrix[0].size();
    
            vector<vector<int>> maxSquares(m, vector<int>(n, 0));
            int maxSide = 0;
    
            for (int i=0; i<m; i++) {
                for (int j=0; j<n; j++) {
                    if (matrix[i][j] == '1') {
                        int minNeigh = INT_MAX;
                        if (i>0) minNeigh = min(minNeigh, maxSquares[i-1][j]);
                        else minNeigh = 0;
                        if (j>0) minNeigh = min(minNeigh, maxSquares[i][j-1]);
                        else minNeigh = 0;
                        if (i>0 && j>0) minNeigh = min(minNeigh, maxSquares[i-1][j-1]);
                        else minNeigh = 0;
                        maxSquares[i][j] = minNeigh + 1;
                        maxSide = max(maxSide, maxSquares[i][j]);
                    }
                }
            }
    
            return maxSide * maxSide;
        }
    };
