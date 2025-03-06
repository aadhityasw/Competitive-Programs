class Solution {
    public:
        long long countBadPairs(vector<int>& nums) {
            map<int, int> store;
    
            for (int i=0; i<nums.size(); i++) {
                int diff = nums[i]-i;
                store[diff] ++;
            }
    
            long long n = nums.size();
            long long ans = (n * (n-1) / 2);
            for (const auto & ele : store) {
                long long cur = ele.second;
                ans -= (cur * (cur-1) / 2);
            }
    
            return ans;
        }
    };
