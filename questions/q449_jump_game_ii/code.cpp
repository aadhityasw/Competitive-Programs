class Solution {
    public:
        int jump(vector<int>& nums) {
            int n = nums.size();
            int pos = 0;
            int numJumps = 0;
    
            while (pos < n) {
                if (pos >= n-1) {
                    return numJumps;
                }
                int reach = pos + nums[pos];
                int maxReachCandidate = pos;
                if (reach >= n-1) {
                    return numJumps+1;
                }
    
                int j=pos+1;
                while (j <= reach) {
                    if (maxReachCandidate+nums[maxReachCandidate] < j+nums[j]) {
                        maxReachCandidate = j;
                    }
                    j++;
                }
    
                pos = maxReachCandidate;
                numJumps++;
            }
    
            return numJumps;
        }
    };
