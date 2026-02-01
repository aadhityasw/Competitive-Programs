class Solution {
public:
    int atmost(vector<int>& nums, int k) {
        int front=0, rear=0;
        int curOdd = 0;
        int count = 0;

        while (rear < nums.size()) {
            if (nums[rear] % 2 == 1) {
                curOdd += 1;
            }

            while (curOdd > k) {
                if (nums[front] % 2 == 1) {
                    curOdd -= 1;
                }
                front ++;
            }

            count += (rear - front + 1);
            rear ++;
        }

        return count;
    }

    int numberOfSubarrays(vector<int>& nums, int k) {
        return atmost(nums, k) - atmost(nums, k-1);
    }
};
