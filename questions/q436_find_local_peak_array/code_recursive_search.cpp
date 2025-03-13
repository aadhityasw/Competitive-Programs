// We do a kind of binary search but still we cover the whole array as we search on both sides after every split


class Solution {
    public:
        bool isPeak(int ind, vector<int>& nums) {
            if (ind == 0 && (nums.size()==1 || nums[ind+1] < nums[ind])) {
                return true;
            }
            if (ind == nums.size()-1 && (nums.size() == 1 || nums[ind-1] < nums[ind])) {
                return true;
            }
            if (ind > 0 && ind < nums.size()-1 && nums[ind] > nums[ind-1] && nums[ind] > nums[ind+1]) {
                return true;
            }
            return false;
        }
        
        int findPeak(int s, int e, vector<int>& nums) {
            if (s>e) {
                return -1;
            }
            if (s == e) {
                return isPeak(s, nums)? s: -1;
            }
            int m = (s+e)/2;
            if (isPeak(m, nums)) {
                return m;
            }
            int ind = findPeak(s, m-1, nums);
            if (ind >= 0) {
                return ind;
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
