class Solution {
    public:
        vector<int> countBits(int n) {
            vector<int> ans;
    
            // Fill for all numbers from 0 to n
            for (int i=0; i<= n; i++) {
                if (i == 0) {
                    ans.push_back(0);
                }
                else {
                    int prev_count = ans[i/2];
                    if (i%2 == 1) {
                        prev_count += 1;
                    }
                    ans.push_back(prev_count);
                }
            }
    
            return ans;
        }
    };
