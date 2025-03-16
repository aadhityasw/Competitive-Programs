class Solution {
    public:
        long long minCost(vector<int>& nums, vector<int>& costs) {
            int n = nums.size();
            vector<int> dp(n, INT_MAX);
            dp[0] = 0;
    
            for (int i=0; i<n; i++) {
                bool sm=false, gr=false;
                for (int j=i+1; j<n; j++) {
                    if (nums[j] >= nums[i] && !gr) {
                        gr=true;
                        dp[j] = min(dp[j], dp[i]+costs[j]);
                    }
                    if (nums[j] < nums[i] && !sm) {
                        sm = true;
                        dp[j] = min(dp[j], dp[i]+costs[j]);
                    }
                    if (sm && gr) {
                        break;
                    }
                }
            }
    
            return dp[n-1];
        }
    };
