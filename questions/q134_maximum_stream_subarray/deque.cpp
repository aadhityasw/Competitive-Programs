// This is for the leetcode version of the problem


class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> store;
        vector<int> ans;

        for (int i=0; i<nums.size(); i++) {
            while (store.size() > 0 && nums[store.back()] <= nums[i]) {
                store.pop_back();
            }
            while (store.size() > 0 && store.front() <= i-k) {
                store.pop_front();
            }
            store.push_back(i);
            
            if (i >= k-1) {
                ans.push_back(nums[store.front()]);
            }
        }

        return ans;
    }
};
