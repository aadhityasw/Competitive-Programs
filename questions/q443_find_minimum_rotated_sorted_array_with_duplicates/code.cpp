class Solution {
    public:
        int findMin(vector<int>& nums) {
            int low = 0, high = nums.size()-1, mid;
            
            while (low < high) {
                mid = (low+high)/2;
                
                if (nums[mid] < nums[high]) {
                    high = mid;
                }
                else if (nums[mid] > nums[high]) {
                    low = mid+1;
                }
                else {
                    // If the mid point is equal, we really cant determine where we are
                    // We just delay this decision by reducing the high point
                    // this does not cause any difference because mid is equal to high so we dont lose this value
                    high = high - 1;
                }
            }
            
            return nums[low];
        }
    };
