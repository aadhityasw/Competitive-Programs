class Solution {
    public:
        int rob(vector<int>& nums) {
            int ans=0;
            int prev=0;
            int cur=0;
    
            if (nums.size() == 1) {
                return nums[0];
            }
            else if (nums.size() == 2) {
                return max(nums[0], nums[1]);
            }
    
            for (int i=0; i<nums.size()-1; i++) {
                int next = max(cur, prev+nums[i]);
                prev = cur;
                cur = next;
            }
            ans = cur;
    
            cur=0;
            prev=0;
            for (int i=nums.size()-1; i>0; i--) {
                int next = max(cur, prev+nums[i]);
                prev = cur;
                cur = next;
            }
    
            ans = max(ans, cur);
            return ans;
        }
    };
