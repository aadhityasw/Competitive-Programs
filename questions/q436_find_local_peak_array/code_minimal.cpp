// Just the minimal barebones code
// Move in the direction of increasing numbers


class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int n = nums.size();
        int l=0, r=n-1;
        
        while (l <= r) {
            int m = l + (r-l)/2;

            if ((m == 0 || nums[m-1] < nums[m]) && (m == n-1 || nums[m+1] < nums[m])) {
                return m;
            }
            else if (m > 0 && nums[m-1] > nums[m]) {
                r = m-1;
            }
            else {
                l = m+1;
            }
        }

        return INT_MIN;
    }
};
