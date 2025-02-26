// Leetcode version

class Solution {
    public:
        int coinChange(vector<int>& coins, int amount) {
            int n = coins.size();
    
            vector<int> store(amount+1, INT_MAX);
            store[0] = 0;
    
            int take, notTake;
    
            for (int i=0; i<n;i++) {
                for (int j=0;j<=amount; j++) {
                    take=INT_MAX;
                    notTake = INT_MAX;
    
                    if (j-coins[i] >= 0) {
                        take = store[j-coins[i]];
                        if (take != INT_MAX) {
                            take++;
                        }
                    }
                    notTake = store[j];
    
                    store[j] = min(take, notTake);
                }
            }
    
            if (store[amount] == INT_MAX) {
                return -1;
            }
            return store[amount];
        }
};
