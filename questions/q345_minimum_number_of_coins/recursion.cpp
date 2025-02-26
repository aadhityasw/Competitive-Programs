class Solution {
    public:
        vector<int> store;
        int coinChange(vector<int>& coins, int amount) {
            store.resize(amount+1, -1);
            coinChangeRecurse(coins, amount, 0);
            if (store[amount] == INT_MAX) {
                return -1;
            }
            return store[amount];
        }
    
        int coinChangeRecurse(vector<int>& coins, int amount, int curSteps) {
            if (amount == 0) {
                store[amount] = 0;
                return 0;
            }
            else if (amount < 0) {
                return INT_MAX;
            }
            else if (store[amount] != -1) {
                return store[amount];
            }
    
            int minVal = INT_MAX;
            for(int i=0;i<coins.size();i++) {
                if (coins[i] > amount) {
                    continue;
                }
    
                minVal = min(coinChangeRecurse(coins, amount-coins[i], curSteps+1), minVal);
            }
    
            if (minVal == INT_MAX) {
                store[amount] = minVal;
            }
            else {
                store[amount] = minVal+1;
            }
            
            return store[amount];
        }
    };
