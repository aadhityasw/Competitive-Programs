class Solution {
    public:
        bool canReach(string s, int minJump, int maxJump) {
            int n = s.length();
            vector<bool> dp(n, false);
            dp[0] = true;
    
            if (s[n-1] == '1') {
                return false;
            }
    
            int prevCount=0;
            // Sliding window is from [i-maxJump, i-minJump]
            for (int i=1; i<n; i++) {
                if (i>=minJump) {
                    prevCount += dp[i-minJump];
                }
                if (i>maxJump) {
                    prevCount -= dp[i-maxJump-1];
                }
                dp[i] = prevCount>0 && (s[i] == '0');
            }
    
            return dp[n-1];
        }
    };
