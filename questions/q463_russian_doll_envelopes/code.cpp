// A bottom - up approach

// Reduces the dimension of the problem to 1D by intelligent sorting and then solves a LIS

class Solution {
    public:
        int maxEnvelopes(vector<vector<int>>& envelopes) {
            int n = envelopes.size();
            // Negate the second dimensiton so that we end up with an order that is increasing by first dim and decreasing by second
            for(int i=0; i<n; i++) {
                envelopes[i][1] = -envelopes[i][1];
            }
            sort(envelopes.begin(), envelopes.end());
    
            // Stores the 2nd dimension of the envelopes in 1st dimension's sorted order
            vector<int> dp(n);
            for(int i=0; i<n; i++) {
                dp[i] = -envelopes[i][1];
            }
    
            // Perform LIS in this dp array and that is our solution
            // The order in DP is such that (i+1)th first dimension is always >= ith first dimension
            // So just a LIS would do the job
            int size=0;
            for (int i=0; i<n; i++) {
                if (dp[i] < dp[0]) {
                    // smaller than the smallest
                    dp[0] = dp[i];
                }
                else if (dp[i] > dp[size]) {
                    // greater than the greatest
                    size++;
                    dp[size] = dp[i];
                }
                else {
                    int l=0,r=size;
                    while (l < r) {
                        int m = l + (r-l)/2;
                        if (dp[i] > dp[m]) {
                            l = m+1;
                        }
                        else {
                            r = m;
                        }
                    }
                    dp[r] = dp[i];
                }
            }
    
            return size+1;
        }
    };
