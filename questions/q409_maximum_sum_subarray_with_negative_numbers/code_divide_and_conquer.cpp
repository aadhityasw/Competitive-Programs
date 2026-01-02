class Solution {
public:
    int maxSum;

    Solution() {
        maxSum = INT_MIN;
    }

    vector<int> getMaxSum(vector<int>& nums, int s, int e) {
        if (s > e) {
            return {0, 0, 0};
        }
        else if (s == e) {
            maxSum = max(maxSum, nums[s]);
            return {nums[s], nums[s], nums[s]};
        }
        else {
            int mid = s + ((e - s) / 2);
            vector<int> left = getMaxSum(nums, s, mid);
            vector<int> right = getMaxSum(nums, mid+1, e);

            maxSum = max(maxSum, left[2]+right[0]);
            maxSum = max(maxSum, left[2]);
            maxSum = max(maxSum, right[0]);

            vector<int> cur = {0, 0, 0};
            cur[0] = max(left[0], left[1]+right[0]);
            cur[1] = left[1] + right[1];
            cur[2] = max(left[2]+right[1], right[2]);
            return cur;
        }
    }

    int maxSubArray(vector<int>& nums) {
        int n = nums.size();

        getMaxSum(nums, 0, n-1);
        return maxSum;
    }
};
