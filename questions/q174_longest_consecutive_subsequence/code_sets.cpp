// Leetcode version of the problem
// Uses sets for constant retrieval, and thereby passes all the test cases

class Solution {
    public:
        int longestConsecutive(vector<int>& nums) {
            unordered_set<int> store(nums.begin(), nums.end());
            int n = nums.size();
            int ans=0;
    
            for (int i=0; i<n; i++) {
                int curEle = nums[i];
                int curCount = 0;
    
                while (store.count(curEle) > 0) {
                    curCount++;
                    store.erase(curEle);
                    curEle++;
                }
    
                curEle = nums[i]-1;
                while (store.count(curEle) > 0) {
                    curCount++;
                    store.erase(curEle);
                    curEle--;
                }
    
                ans = max(ans, curCount);
            }
    
            return ans;
        }
    };
