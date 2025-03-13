class Solution {
    public:
        int rob(vector<int>& nums) {
            int prev = 0;
            int cur = 0;
            for (int i=0; i<nums.size(); i++) {
                int next = max(cur, prev+nums[i]);
                prev = cur;
                cur = next;
            }
    
            return cur;
        }
    };
