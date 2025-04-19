class Solution {
    public:
        int trap(vector<int>& height) {
            int n = height.size();
            int totalWater = 0;
    
            int l=0, r=n-1;
            int lMax = INT_MIN, rMax = INT_MIN;
    
            while (l<r) {
                if (lMax < height[l]) {
                    lMax = height[l];
                }
                if (rMax < height[r]) {
                    rMax = height[r];
                }
    
                if (height[l] <= height[r]) {
                    // Move left pointer
                    totalWater += max(0, min(lMax, rMax)-height[l]);
                    l++;
                }
                else {
                    // Move right pointer
                    totalWater += max(0, min(lMax, rMax)-height[r]);
                    r--;
                }
            }
    
            return totalWater;
        }
    };
