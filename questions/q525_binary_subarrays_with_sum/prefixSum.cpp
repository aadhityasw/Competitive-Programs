class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        unordered_map<int, int> store;
        int curSum = 0;
        int count = 0;

        store[0] = 1;

        for (int i=0; i<nums.size(); i++) {
            curSum += nums[i];
            if (curSum >= goal) {
                count += store[curSum - goal];
            }
            store[curSum] += 1;
        }

        return count;
    }
};
