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
        int globalPtr;
    
        int extractNextNum(string traversal) {
            int ans=0;
            while (globalPtr < traversal.length() && traversal[globalPtr] == '-') {
                globalPtr++;
            }
            while (globalPtr < traversal.length()) {
                if (traversal[globalPtr] >= 48 && traversal[globalPtr]<=57) {
                    ans = ans*10 + (int)(traversal[globalPtr]-48);
                    globalPtr++;
                }
                else {
                    break;
                }
            }
            return ans;
        }
    
        void processTree (TreeNode* root, int curLevel, string traversal) {
            while (globalPtr < traversal.length()) {
                int numDashes = 0, pos=globalPtr;
                while (pos < traversal.length() && traversal[pos] == '-') {
                    numDashes ++;
                    pos++;
                }
                
                if (numDashes == curLevel+1) {
                    TreeNode *newNode = new TreeNode(extractNextNum(traversal));
                    if (root->left == nullptr) {
                        root->left = newNode;
                        processTree(root->left, curLevel+1, traversal);
                    }
                    else {
                        root->right = newNode;
                        processTree(root->right, curLevel+1, traversal);
                    }
                }
                else if (numDashes < curLevel+1) {
                    return;
                }
                else {
                    if (root->right != nullptr) {
                        processTree(root->right, curLevel+1, traversal);
                    }
                    else {
                        processTree(root->left, curLevel+1, traversal);
                    }
                }
            }
        }
    
        TreeNode* recoverFromPreorder(string traversal) {
            globalPtr = 0;
            TreeNode *root = new TreeNode(extractNextNum(traversal));
    
            processTree(root, 0, traversal);
            return root;
        }
    };
