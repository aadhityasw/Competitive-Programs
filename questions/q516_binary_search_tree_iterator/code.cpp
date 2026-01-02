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

#include<stack>

class BSTIterator {
public:
    stack<TreeNode*> callStack;

    BSTIterator(TreeNode* root) {
        processSmallest(root);
    }
    
    int next() {
        if (callStack.empty()) {
            return -1;
        }

        TreeNode* ptr = callStack.top();
        callStack.pop();
        if (ptr->right != nullptr) {
            processSmallest(ptr->right);
        }

        return ptr->val;
    }
    
    bool hasNext() {
        return (!callStack.empty());
    }

    void processSmallest(TreeNode* ptr) {
        while (ptr != nullptr) {
            callStack.push(ptr);
            ptr = ptr->left;
        }
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
