// This is the solution to leetcode's version of the problem
// Leetcode Q: 54

#include<vector>
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m=matrix.size(), n=matrix[0].size();

        int top=0, bottom=m-1, left=0, right=n-1, i;
        vector<int> ans;

        while (top<=bottom && left<=right) {
            // Move left to right
            if (top <= bottom) {
                for (i=left; i<=right; i++) {
                    ans.push_back(matrix[top][i]);
                }
            }
            top++;

            // Move top to bottom
            if (left <= right) {
                for (i=top;i<=bottom;i++) {
                    ans.push_back(matrix[i][right]);
                }
            }
            right--;

            // Move right to left
            if (top <= bottom) {
                for (i=right;i>=left;i--) {
                    ans.push_back(matrix[bottom][i]);
                }
            }
            bottom--;

            // Move bottom to top
            if (left <= right) {
                for (i=bottom;i>=top;i--) {
                    ans.push_back(matrix[i][left]);
                }
            }
            left++;
        }

        return ans;
    }
};
