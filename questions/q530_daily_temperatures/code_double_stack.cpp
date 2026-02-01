class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int, int>> store;
        vector<int> ans(temperatures.size(), 0);

        for (int i=temperatures.size()-1; i>=0; i--) {
            int numDays = 1;
            while (!store.empty() && store.top().first <= temperatures[i]) {
                numDays += store.top().second;
                store.pop();
            }

            if (!store.empty()) {
                ans[i] = numDays;
            }

            store.push({temperatures[i], numDays});
        }

        return ans;
    }
};
