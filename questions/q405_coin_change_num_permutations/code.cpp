class Solution {
    public:
        int change(int amount, vector<int>& coins) {
            int n = coins.size();
            vector<double> counts(amount+1, 0);
    
            if (amount == 0) {
                return 1;
            }
            
            for (int i=0; i<n; i++) {
                for (int j=1; j<=amount; j++) {
                    if (j > coins[i]) {
                        counts[j] += counts[j - coins[i]];
                    }
                    else if (j == coins[i]) {
                        counts[j]++;
                    }
                }
            }
    
            return counts[amount];
        }
    };
