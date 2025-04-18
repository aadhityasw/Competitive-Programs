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

	int maxPathSumValue;

	int traverseTreeAndFindMaxSum(TreeNode* ptr) {
		
		// If the ptr is null, then we return INT_MIN
		if (ptr == nullptr) {
			return INT_MIN;
		}

		// Get the maximum path sum of left and right nodes
		int leftSum = traverseTreeAndFindMaxSum(ptr->left);
		int rightSum = traverseTreeAndFindMaxSum(ptr->right);

		maxPathSumValue = max(maxPathSumValue, leftSum);
		maxPathSumValue = max(maxPathSumValue, rightSum);
        if (leftSum > INT_MIN) {
            maxPathSumValue = max(maxPathSumValue, leftSum+ptr->val);
        }
        if (rightSum > INT_MIN) {
            maxPathSumValue = max(maxPathSumValue, rightSum+ptr->val);
        }
        if (rightSum > INT_MIN && leftSum > INT_MIN) {
            maxPathSumValue = max(maxPathSumValue, leftSum+ptr->val+rightSum);
        }
		maxPathSumValue = max(maxPathSumValue, ptr->val);
		
		

		int curMaxValueToPropagate = ptr->val;
		if (leftSum > rightSum) {
			curMaxValueToPropagate = max(curMaxValueToPropagate, leftSum+ptr->val);
		}
		else if (rightSum > leftSum) {
			curMaxValueToPropagate = max(curMaxValueToPropagate, rightSum+ptr->val);
		}
		else if (leftSum != INT_MIN && rightSum != INT_MIN && leftSum == rightSum) {
			curMaxValueToPropagate = max(curMaxValueToPropagate, leftSum+ptr->val);
        }

        return curMaxValueToPropagate;
	}


	int maxPathSum(TreeNode* root) {
		maxPathSumValue = INT_MIN;
		traverseTreeAndFindMaxSum(root);
		
		return maxPathSumValue;
	}
};
