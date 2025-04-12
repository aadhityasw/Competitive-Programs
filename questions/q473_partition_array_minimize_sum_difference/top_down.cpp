// Causes TLE


class Solution {
    public:
    
        void findMinDifference(vector<int> &nums, int s1, int s2, int c1, int idx, int &min_sum)
        {
            if(idx == nums.size())
            {
                if(c1 != nums.size()/2)
                {
                    return ;
                }
    
                min_sum = min(min_sum, abs(s1 - s2));
                return ;
            }   
    
            s1 += nums[idx];
            findMinDifference(nums, s1, s2, c1+1, idx+1, min_sum);
            s1 -= nums[idx];
            s2 += nums[idx];
            findMinDifference(nums, s1, s2, c1, idx+1, min_sum);
            s2 -= nums[idx];
        }
    
        int minimumDifference(vector<int>& nums) {
            int n = nums.size();
    
            int min_sum = INT_MAX;
            findMinDifference(nums, 0, 0, 0, 0, min_sum);    
            return min_sum;
        }
    };
