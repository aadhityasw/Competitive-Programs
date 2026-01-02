class Solution {
public:
    vector<int> store;
    int n;

    Solution(vector<int>& nums) {
        n = nums.size();
        store = nums;
    }
    
    vector<int> reset() {
        return store;
    }
    
    vector<int> shuffle() {
        vector<int> nums(store.begin(), store.end());

        for (int i=0; i<n; i++) {
            int pos = i + rand()%(n-i);
            swap(nums[i], nums[pos]);
        }
        
        return nums;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */
