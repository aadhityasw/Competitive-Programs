// This is not a perfect solution as it causes Time limit exceeded for some test cases

// This is for the leetcode 128, version of the problem

class Solution {
    public:
        int longestConsecutive(vector<int>& nums) {
            vector<vector<int>> store(10);
            int n = nums.size();
            int ovMin = INT_MAX, ovMax = INT_MIN;
            if (n == 0) {
                return 0;
            }
    
            for (int i=0; i<n; i++) {
                store[abs(nums[i])%10].push_back(nums[i]);
                ovMin = min(ovMin, nums[i]);
                ovMax = max(ovMax, nums[i]);
            }
    
            int ans = 0;
            int curLeft=0,curRight=0;
            while (curRight <= ovMax || curLeft >= ovMin) {
                int curCountLeft = 0, curCountRight=0;
    
                while (curRight <= ovMax && find(store[curRight%10].begin(), store[curRight%10].end(), curRight) != store[curRight%10].end()) {
                    curCountRight++;
                    curRight++;
                }
    
                while (curLeft >= ovMin && find(store[abs(curLeft)%10].begin(), store[abs(curLeft)%10].end(), curLeft) != store[abs(curLeft)%10].end()) {
                    curCountLeft++;
                    curLeft--;
                }
    
                if (curCountLeft > 0 && curRight-curCountRight == curLeft+curCountLeft && curRight-curCountRight == 0) {
                    ans = max(ans, curCountLeft+curCountRight-1);
                }
                else {
                    ans = max(ans, curCountLeft);
                    ans = max(ans, curCountRight);
                }
    
                curCountLeft = 0;
                curCountRight = 0;
                curLeft--;
                curRight++;
            }
    
            return ans;
        }
    };
