class Solution {
    public:
        int findNum(int target, vector<int>& nums) {
            int low = 0, high=nums.size()-1, mid=0;
            while (low < high) {
                mid = (low+high)/2;
                if (nums[mid] == target) {
                    return mid;
                }
                else if (nums[mid] < target) {
                    low = mid+1;
                }
                else {
                    high = mid-1;
                }
            }
            
            return (nums[low] == target)? low : -1;
        }
        
        int findStartRange(int target, int ind, vector<int>& nums) {
            int low = 0, high = ind, mid=0;
            while (low < high) {
                mid = (low+high)/2;
                if (nums[mid] < nums[ind]) {
                    low = mid+1;
                }
                else {
                    high = mid;
                }
            }
            return low;
        }
        
        int findEndRange(int target, int ind, vector<int>& nums) {
            int low = ind, high = nums.size()-1, mid=0;
            while (low < high) {
                mid = (low+high)/2;
                if (nums[mid] > nums[ind]) {
                    high = mid-1;
                }
                else {
                    low = mid;
                }
                if (high == low+1) {
                    return (nums[high] == nums[ind]) ? high : low;
                }
            }
            return low;
        }
        
        vector<int> searchRange(vector<int>& nums, int target) {
            if (nums.size() == 0) {
                return {-1, -1};
            }
            int ind = findNum(target, nums);
            if (ind == -1) {
                return {-1, -1};
            }
            return {
                findStartRange(target, ind, nums),
                findEndRange(target, ind, nums)
            };
        }
    };
