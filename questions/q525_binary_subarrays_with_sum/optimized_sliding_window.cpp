// Single Pass Sliding Window
// (A sort of combination of both Prefix Sum and the dual sliding window approaches)

class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        int front=0, rear=0;
        int curSum = 0, pZero=0;
        int count = 0;

        while (rear < nums.size()) {
            curSum += nums[rear];

            while (curSum > goal && front < rear) {
                curSum -= nums[front++];
                pZero = 0;
            }

            while (curSum == goal && front < rear && nums[front] == 0) {
                front ++;
                pZero ++;
            }

            if (curSum == goal) {
                count += (pZero + 1);
            }
            
            rear ++;
        }

        return count;
    }
};
