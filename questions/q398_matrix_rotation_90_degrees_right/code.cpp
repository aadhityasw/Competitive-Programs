class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size(), temp;

        // transpose
        for (int i=0;i<n;i++) {
            for(int j=0;j<i;j++) {
                temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        // horizontal revese
        for (int i=0;i<n;i++) {
            for(int j=0;j<int(n/2);j++) {
                temp = matrix[i][j];
                matrix[i][j] = matrix[i][n-j-1];
                matrix[i][n-j-1] = temp;
            }
        }
    }
};
