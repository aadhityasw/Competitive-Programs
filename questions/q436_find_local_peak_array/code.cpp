// This is an improvement over the other code
// We just have to find any local maxima, so if the mid point is not a maxima, move in the direction of the greater number to get to the maxima


class Solution {
    public:
        int determineNextMove(int ind, vector<int>& nums) {
            if (ind == 0) {
                if (nums.size()==1 || nums[ind+1] < nums[ind]) {
                    return 0;
                }
                return 1;
            }
            if (ind == nums.size()-1) {
                if (nums.size() == 1 || nums[ind-1] < nums[ind]) {
                    return 0;
                }
                return -1;
            }
            if (nums[ind] > nums[ind-1] && nums[ind] > nums[ind+1]) {
                return 0;
            }
            if (nums[ind] > nums[ind-1]) {
                return 1;
            }
            return -1;
        }
        
        int findPeak(int s, int e, vector<int>& nums) {
            if (s>e) {
                return -1;
            }
            if (s == e) {
                return determineNextMove(s, nums) == 0? s: -1;
            }
            int m = (s+e)/2;
            int nextMove = determineNextMove(m, nums);
            if (nextMove == 0) {
                return m;
            }
            else if (nextMove < 0) {
                return findPeak(s, m-1,  nums);
            }
            return findPeak(m+1, e, nums);
        }
        
        int findPeakElement(vector<int>& nums) {
            int n = nums.size();
            int low = 0, high = n-1;
            int ind = findPeak(0, high, nums);
            return ind;
        }
    };
