class Solution {
public:
    int slidingWindowAtMostSum(vector<int>& nums, int goal) {
        if (goal < 0) {
            return 0;
        }

        int front=-1, rear=0;
        int curSum = 0;

        // Count measures the number of sub-arrays of length at least goal
        int count = 0;

        while (rear < nums.size()) {
            curSum += nums[rear];

            while (front <= rear && curSum > goal) {
                front++;
                curSum -= nums[front];
            }

            // Say the window is of size 3, we add the window length as we can form 3 sub-arrays starting from front.
            count += (rear - front);
            rear ++;
        }

        return count;
    }

    int numSubarraysWithSum(vector<int>& nums, int goal) {
        return slidingWindowAtMostSum(nums, goal) - slidingWindowAtMostSum(nums, goal-1);
    }
};
