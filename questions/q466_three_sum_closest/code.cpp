class Solution {
    public:
        int twoSum(int s, vector<int>& nums, int target) {
            int e = nums.size()-1;
            int closestSum = INT_MAX;
    
            while (s<e) {
                int curS = nums[s] + nums[e];
                if (closestSum == INT_MAX || abs(curS-target) < abs(closestSum-target)) {
                    closestSum = curS;
                }
    
                if (curS < target) {
                    s++;
                }
                else {
                    e--;
                }
            }
    
            return closestSum;
        }
    
        int threeSumClosest(vector<int>& nums, int target) {
            int closestSum = INT_MAX;
            int n = nums.size();
            sort(nums.begin(), nums.end());
    
            for (int i=0; i<n-2; i++) {
                int curS = twoSum(i+1, nums, target-nums[i]);
                if (closestSum == INT_MAX || abs(curS+nums[i]-target) < abs(closestSum - target)) {
                    closestSum = curS+nums[i];
                }
            }
    
            return closestSum;
    
        }
    };
