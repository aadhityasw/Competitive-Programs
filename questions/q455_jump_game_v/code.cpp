class Solution {
    public:
        int maxJumps(vector<int>& arr, int d) {
            int n = arr.size();
            vector<int> dp(n, 0);
            int maxCover = 0;
    
            for (int i=0; i<n; i++) {
                search(arr, dp, i, d);
                maxCover = max(maxCover, dp[i]);
            }
    
            return maxCover;
        }
    
        int search(vector<int>& arr, vector<int>& dp, int pos, int d) {
            if (dp[pos] > 0) {
                return dp[pos];
            }
    
            int maxCover = 1;
    
            // Left shift
            for (int i=pos-1; i>= max(pos-d, 0); i--) {
                if (arr[pos] <= arr[i]) {
                    break;
                }
                maxCover = max(maxCover, 1+search(arr, dp, i, d));
            }
    
            // right shift
            for (int i=pos+1; i<=min((int)arr.size()-1, pos+d); i++) {
                if (arr[pos] <= arr[i]) {
                    break;
                }
                maxCover = max(maxCover, 1+search(arr, dp, i, d));
            }
    
            dp[pos] = maxCover;
            return dp[pos];
        }
    };
