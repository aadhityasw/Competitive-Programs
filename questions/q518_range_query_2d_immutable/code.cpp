class NumMatrix {
public:
    int m, n;
    vector<vector<int>> cumSum;
    NumMatrix(vector<vector<int>>& matrix) {
        m = matrix.size();
        n = matrix[0].size();
        cumSum.resize(m+1, vector<int>(n+1));

        vector<int> verSum(n+1, 0);

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                cumSum[i+1][j+1] = cumSum[i+1][j] + verSum[j+1] + matrix[i][j];
                verSum[j+1] += matrix[i][j];
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        // Total - left - right + (addition of part that was removed twice)
        return cumSum[row2+1][col2+1] - cumSum[row2+1][col1] - cumSum[row1][col2+1] + cumSum[row1][col1];
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */
