// This is for the leetcode version of the problem


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
        void traverseLeftBoundary(TreeNode* root, vector<int>& boundary) {
            if (root == nullptr || (root->left == nullptr && root->right == nullptr)) {
                return;
            }
    
            boundary.push_back(root->val);
            if (root->left != nullptr) {
                traverseLeftBoundary(root->left, boundary);
            }
            else {
                traverseLeftBoundary(root->right, boundary);
            }
        }
    
        void traverseAndFindChildren(TreeNode* root, vector<int>& boundary) {
            if (root == nullptr) {
                return;
            }
            if (root->left == nullptr && root->right == nullptr) {
                boundary.push_back(root->val);
            }
    
            traverseAndFindChildren(root->left, boundary);
            traverseAndFindChildren(root->right, boundary);
        }
    
        void traverseRightBoundary(TreeNode* root, vector<int>& boundary) {
            if (root == nullptr || (root->left == nullptr && root->right == nullptr)) {
                return;
            }
    
            if (root->right != nullptr) {
                traverseRightBoundary(root->right, boundary);
            }
            else {
                traverseRightBoundary(root->left, boundary);
            }
            boundary.push_back(root->val);
        }
    
        vector<int> boundaryOfBinaryTree(TreeNode* root) {
            vector<int> boundary;
            if (root != nullptr) {
                boundary.push_back(root->val);
            }
            traverseLeftBoundary(root->left, boundary);
            traverseAndFindChildren(root->left, boundary);
            traverseAndFindChildren(root->right, boundary);
            traverseRightBoundary(root->right, boundary);
    
            return boundary;
        }
    };
