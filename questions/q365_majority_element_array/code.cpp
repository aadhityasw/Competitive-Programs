class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int i=0,ans, freq = 0;

        while (i < nums.size())
        {
            if (freq == 0)
            {
                ans = nums[i];
            }

            if (nums[i] == ans)
            {
                freq++;
            }
            else
            {
                freq--;
            }
            i++;
        }

        return ans;
    }
};