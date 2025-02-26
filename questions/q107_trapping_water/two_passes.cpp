// Uses memoization and passes through the array two times

class Solution {
public:
    int trap(vector<int>& height) {
        int i=0, water=0, rMax=0, lMax=0;
        int* leftMax = new int[height.size()];

        lMax = height[0];
        while (i < height.size()) {
            if (lMax < height[i]) {
                lMax = height[i];
            }
            leftMax[i] = lMax;
            i++;
        }

        i = height.size()-1;
        rMax = height[i];
        while (i >= 0) {
            if (rMax < height[i]) {
                rMax = height[i];
            }

            if (leftMax[i] < rMax) {
                water += (leftMax[i] - height[i]);
            }
            else {
                water += (rMax - height[i]);
            }

            i--;
        }

        return water;
    }
};