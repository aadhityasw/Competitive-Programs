// Uses Dequeue, and efficient sliding window manipulation


class Solution {
    public:
        int maxResult(vector<int>& nums, int k) {
            int n = nums.size();
            deque<int> cache;
            vector<int> dp(n, INT_MIN);
            dp[0] = nums[0];
            cache.push_back(0);
    
            for (int i=1; i<n; i++) {
                while(!cache.empty() && cache.front() < (i-k)) {
                    cache.pop_front();
                }
                dp[i] = dp[cache.front()] + nums[i];
                while (!cache.empty() && dp[cache.back()] < dp[i]) {
                    cache.pop_back();
                }
                cache.push_back(i);
            }
    
            return dp[n-1];
        }
    };
