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
    int maxLevelSum(TreeNode* root) {
        int maxLevel = 0, maxSum = INT_MIN;
        int curLevelId = 0, curSum = 0;
        vector<TreeNode*> *curLevel = new vector<TreeNode*> {root};
        vector<TreeNode*> *nextLevel;

        while (curLevel->size() > 0) {
            nextLevel = new vector<TreeNode*> {};
            curLevelId ++;
            curSum = 0;

            for (TreeNode* ptr : *curLevel) {
                curSum += ptr->val;
                if (ptr->left != nullptr) {
                    nextLevel->push_back(ptr->left);
                }
                if (ptr->right != nullptr) {
                    nextLevel->push_back(ptr->right);
                }
            }

            if (curSum > maxSum) {
                maxLevel = curLevelId;
                maxSum = curSum;
            }

            delete curLevel;
            curLevel = nextLevel;
        }

        return maxLevel;
    }
};
