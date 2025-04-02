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
        void traverseTree(TreeNode* root, int curLevel, vector<int>& rightSideView) {
            if (root == nullptr) {
                return;
            }
            if (curLevel > rightSideView.size()) {
                rightSideView.push_back(root->val);
            }
    
            if (root->right != nullptr) {
                traverseTree(root->right, curLevel+1, rightSideView);
            }
            if (root->left != nullptr) {
                traverseTree(root->left, curLevel+1, rightSideView);
            }
        }
    
        vector<int> rightSideView(TreeNode* root) {
            vector<int> rightSideView;
            traverseTree(root, 1, rightSideView);
            return rightSideView;
        }
    };
