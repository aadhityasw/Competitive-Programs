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
        int closestValue(TreeNode* root, double target) {
            int nodeVal = root->val;
            double minDiff = abs(root->val - target);
            
            TreeNode* ptr = root;
            while (ptr != nullptr) {
                if (abs(ptr->val - target) < minDiff) {
                    minDiff = abs(ptr->val - target);
                    nodeVal = ptr->val;
                }
                else if (abs(ptr->val - target) == minDiff) {
                    nodeVal = min(nodeVal, ptr->val);
                }
                if (ptr->val > target) {
                    ptr = ptr->left;
                }
                else {
                    ptr = ptr->right;
                }
            }
            
            return nodeVal;
        }
    };
