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
        vector<vector<int>> verticalOrder(TreeNode* root) {
            if (root == nullptr) {
                return {};
            }
    
            map<int, vector<int>> levelToOrder;
            queue<pair<TreeNode*, int>> frontier;
            frontier.push(make_pair(root, 0));
            int minOrder, maxOrder;
            minOrder = INT_MAX;
            maxOrder = INT_MIN;
    
            // We do a BFS
            // Mainly because there can be 2 values at the same level at the same order
            // eg : root->left->right  and root->right->left
            while (!frontier.empty()) {
                TreeNode* ptr = frontier.front().first;
                int curOrder = frontier.front().second;
                frontier.pop();
    
                levelToOrder[curOrder].push_back(ptr->val);
                minOrder = min(minOrder, curOrder);
                maxOrder = max(maxOrder, curOrder);
    
                if (ptr->left != nullptr) {
                    frontier.push(make_pair(ptr->left, curOrder-1));
                }
                if (ptr->right != nullptr) {
                    frontier.push(make_pair(ptr->right, curOrder+1));
                }
            }
    
            vector<vector<int>> ans;
            for (int i=minOrder; i<=maxOrder; i++) {
                ans.push_back(levelToOrder[i]);
            }
    
            return ans;
        }
    };
