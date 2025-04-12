class Solution {
    public:
        int climbStairs(int n) {
            int prevCount = 1;
            int curCount = 0;
            for (int i=0; i<=n; i++) {
                curCount += prevCount;
                prevCount = curCount - prevCount;
            }
    
            return curCount;
        }
    };
