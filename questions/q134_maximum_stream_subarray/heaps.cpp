// This is for the leetcode version of the problem


class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        priority_queue<pair<int, int>, vector<pair<int, int>>> store;
        vector<int> ans;

        for (int i=0; i<k; i++) {
            store.push({nums[i], i});
        }
        ans.push_back(store.top().first);

        for (int i=k; i<nums.size(); i++) {
            store.push({nums[i], i});

            while (store.top().second <= i-k) {
                store.pop();
            }
            ans.push_back(store.top().first);
        }

        return ans;
    }
};
