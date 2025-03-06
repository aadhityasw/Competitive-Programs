class Solution {
    public:
        int findPivot(int s, int e, vector<int>& nums) {
            if (s == e) {
                return s;
            }
            else if (s == e-1) {
                if (nums[s] > nums[e]) {
                    return e;
                }
                return s;
            }
            else {
                int mid = (s+e)/2;
                if (nums[mid] > nums[s]) {
                    return findPivot(mid, e, nums);
                }
                return findPivot(s, mid, nums);
            }
        }
    
        int findNum(int s, int e, int target, vector<int>& nums) {
            if (s == e) {
                if (nums[s] == target) {
                    return s;
                }
                return -1;
            }
    
            if (s > e) {
                return -1;
            }
    
            int mid = (s+e)/2;
            if (nums[mid] < target) {
                return findNum(mid+1, e, target, nums);
            }
            else if (nums[mid] > target) {
                return findNum(s, mid, target, nums);
            }
            else {
                return mid;
            }
        }
    
        int search(vector<int>& nums, int target) {
            int pivot;
            if (nums[nums.size()-1] > nums[0]) {
                pivot = 0;
            }
            else {
                pivot = findPivot(0, nums.size()-1, nums);
            }
            int pos;
    
            if (target < nums[nums.size()-1]) {
                return findNum(pivot, nums.size()-1, target, nums);
            }
            else if (target > nums[nums.size()-1]) {
                return findNum(0, pivot-1, target, nums);
            }
            else {
                return nums.size()-1;
            }
        }
    };
