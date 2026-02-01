class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l=0, r=nums.size()-1, m=0;

        while (l <= r) {
            m = l + (r-l)/2;

            if (nums[m] == target) {
                return m;
            }
            else if (nums[m] > target) {
                if (m == 0 || nums[m-1] < target) {
                    return m;
                }
                else {
                    r = m-1;
                }
            }
            else {
                if (m == nums.size()-1 || nums[m+1] > target) {
                    return m+1;
                }
                else {
                    l = m+1;
                }
            }
        }

        return nums.size();
    }
};
