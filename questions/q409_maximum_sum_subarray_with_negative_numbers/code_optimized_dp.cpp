class Solution {
    public:
        int maxSubArray(vector<int>& nums) {
            int curSubArrayMax = nums[0];
            int ans = curSubArrayMax;
            for (int i=1; i<nums.size(); i++) {
                curSubArrayMax = max(curSubArrayMax,0) + nums[i];
                ans = max(ans, curSubArrayMax);
            }
            return ans;
        }
    };
