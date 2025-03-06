// This solution is incomplete as it fails for when there are negative integers.
// We assume the minimum element is 0 and allocate that if there is no element on the left or right in the leaf nodes
// Presense of negative integers complicates the problem
// Need to set the minimum value to -1e5 and modify the recurseSum function completely to accomodate negative integers.

// This currently passes half of the test cases in leetcode



class Node {
    public:
    int leftSum, rightSum, fullSum;
    Node() {
        leftSum=0;
        rightSum=0;
        fullSum=0;
    }

    Node(int l, int r, int f) {
        leftSum=l;
        rightSum=r;
        fullSum=f;
    }
};

class Solution {
public:
    int ans;

    Node* recurseSum(int start, int end, vector<int>& nums) {
        if (start>end) {
            Node *ptr = new Node(0, 0, 0);
            return ptr;
        }
        else if (start == end) {
            Node *ptr = new Node(0, nums[start], nums[start]);
            return ptr;
        }

        int mid = (start+end)/2;
        Node *left = recurseSum(start, mid-1, nums);
        Node *right = recurseSum(mid+1, end, nums);

        int curMaxSum = max(
            max(left->leftSum, right->rightSum),
            nums[mid] + max(
                0,
                max(left->fullSum, left->rightSum)
            ) + max(
                0,
                max(right->leftSum, right->fullSum)
            )
        );
        ans = max(ans, curMaxSum);
        int leftSideSum = (mid == start)? nums[mid] : max(left->leftSum + max(0, nums[mid]), left->fullSum);
        int rightSideSum = (mid == end)? nums[mid] : max(right->rightSum + max(0, nums[mid]), right->fullSum);
        Node *ptr = new Node(leftSideSum, rightSideSum, (left->fullSum + nums[mid] + right->fullSum));
        return ptr;
    }

    int maxSubArray(vector<int>& nums) {
        int start = 0,end=nums.size()-1;
        ans = nums[0];
        Node *root = recurseSum(start, end, nums);
        return max(ans, max(max(root->leftSum, root->rightSum), root->fullSum));
    }
};
