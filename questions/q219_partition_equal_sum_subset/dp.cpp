// This is for the leetcode version of the problem


class Solution {
    public:
        bool canPartition(vector<int>& nums) {
            int totalSum = 0;
            int n = nums.size();
    
            for (int num : nums) {
                totalSum += num;
            }
            
            if (totalSum % 2 == 1) {
                return false;
            }
    
            vector<vector<bool>> dp(n+1, vector<bool>((totalSum/2) + 1, false));
            dp[0][0] = true;
    
            for (int i=1; i<n+1; i++) {
                for (int j = 0; j<=totalSum/2; j++) {
                    dp[i][j] = dp[i-1][j];
                    if (j >= nums[i-1]) {
                        dp[i][j] = dp[i][j] || dp[i-1][j - nums[i-1]];
                    }
                }
            }
    
            return dp[n-1][totalSum/2];
        }
    };
