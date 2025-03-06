class Solution {
    public:
        int search(vector<int>& nums, int target) {
            int s = 0;
            int e = nums.size()-1;
            int m;
    
            while (s <= e) {
                m = (s+e)/2;
    
                if (s == e) {
                    if (nums[s] == target) {
                        return s;
                    }
                    return -1;
                }
                
                if (target == nums[m]) {
                    return m;
                }
                
                if (nums[m] >= nums[s]) {
                    if (target >= nums[s] && target < nums[m]) {
                        e = m-1;
                    }
                    else {
                        s = m+1;
                    }
                }
                else {
                    if (target >= nums[s] || target < nums[m]) {
                        e = m-1;
                    }
                    else {
                        s = m+1;
                    }
                }
            }
            return -1;
        }
    };
