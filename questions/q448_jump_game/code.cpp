class Solution {
    public:
        bool canJump(vector<int>& nums) {
            int i=0,reach=0;
    
            while (i < nums.size())
            {
                if (i+nums[i] > reach)
                {
                    reach = i+nums[i];
                }
    
                if (reach >= nums.size()-1)
                {
                    return true;
                }
    
                if (i >= reach)
                {
                    break;
                }
    
                i++;
            }
            return false;
        }
    };
