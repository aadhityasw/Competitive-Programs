/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    public:
        int* search(TreeNode* root) {
            if (root == nullptr) {
                int* ans = new int[2]{0, 0};
                return ans;
            }
            int *left = search(root->left);
            int *right = search(root->right);
            int *ans = new int[2]{
                left[1] + root->val + right[1],
                max(left[0], left[1]) + max(right[0], right[1])
            };
            return ans;
        }
    
        int rob(TreeNode* root) {
            int *ans = search(root);
            return max(ans[0], ans[1]);
        }
    };
