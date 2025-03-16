class Solution {
    public:
        int maxResult(vector<int>& nums, int k) {
            int n = nums.size();
            vector<int> dp(n, INT_MAX);
            priority_queue<vector<int>> cache;
            dp[0] = nums[0];
            cache.push({dp[0], 0});
    
            for (int i=1; i<n; i++) {
                while(cache.top()[1] < (i-k)) {
                    cache.pop();
                }
                dp[i] = cache.top()[0] + nums[i];
                cache.push({dp[i], i});
            }
    
            return dp[n-1];
        }
    };
