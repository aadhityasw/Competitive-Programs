// Top Down approach
// Causes TLE in leetcode

class Solution {
    public:
        int nestDolls(int pos, vector<int>& dp, vector<vector<int>>& envelopes) {
            if (dp[pos] != 0) {
                return dp[pos];
            }
    
            int maxNest = 0;
            for (int i=pos+1; i<dp.size(); i++) {
                if (envelopes[i][0] > envelopes[pos][0] && envelopes[i][1] > envelopes[pos][1]) {
                    maxNest = max(maxNest, nestDolls(i, dp, envelopes));
                }
            }
            dp[pos] = 1 + maxNest;
            return dp[pos];
        }
    
        int maxEnvelopes(vector<vector<int>>& envelopes) {
            sort(envelopes.begin(), envelopes.end());
    
            int n = envelopes.size();
            vector<int> dp(n, 0);
            int maxNest=0;
    
            for (int i=0; i<n; i++) {
                if (dp[i] == 0) {
                    maxNest = max(maxNest, nestDolls(i, dp, envelopes));
                }
            }
    
            return maxNest;
        }
    };
