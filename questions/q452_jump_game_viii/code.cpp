// Uses DP but along with stacks to store the previous numbers to get the smaller and greater numbers


class Solution {
    public:
        long long minCost(vector<int>& nums, vector<int>& costs) {
            int n = nums.size();
            vector<long long> dp(n, LONG_MAX);
            dp[0] = 0;
            stack<int> smallerNums;
            stack<int> greaterNums;
            smallerNums.push(0);
            greaterNums.push(0);
    
            for (int i=1; i<n; i++) {
                while (smallerNums.size()>0 && nums[i] >= nums[smallerNums.top()]) {
                    dp[i] = min(dp[i], dp[smallerNums.top()]+costs[i]);
                    smallerNums.pop();
                }
                while (greaterNums.size()>0 && nums[i] < nums[greaterNums.top()]) {
                    dp[i] = min(dp[i], dp[greaterNums.top()]+costs[i]);
                    greaterNums.pop();
                }
    
                smallerNums.push(i);
                greaterNums.push(i);
            }
    
            return dp[n-1];
        }
    };
