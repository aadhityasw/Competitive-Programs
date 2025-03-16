class Solution {
    public:
        int minJumps(vector<int>& arr) {
            int n = arr.size();
            map<int, vector<int>> numToInd;
    
            for (int i=0; i<n; i++) {
                if (numToInd.find(arr[i]) == numToInd.end()) {
                    numToInd[arr[i]] = {i};
                }
                else {
                    numToInd[arr[i]].push_back(i);
                }
            }
            
            vector<int> dp(n, INT_MAX);
            dp[0] = 0;
            queue<int> frontier;
            frontier.push(0);
    
            // If we have visited a cell using BFS, it means that we have filled the cell with the minimum number of steps already, so we will refrain from visiting this again.
            while (frontier.size()>0) {
                int curInd = frontier.front();
                frontier.pop();
    
                if (curInd+1 < n) {
                    if (dp[curInd+1] == INT_MAX) {
                        frontier.push(curInd+1);
                        dp[curInd+1] = dp[curInd]+1;
                    }
                    if (curInd+1 == n-1) {
                        return dp[curInd+1];
                    }
                }
    
                if (curInd-1 >= 0) {
                    if (dp[curInd-1] == INT_MAX) {
                        frontier.push(curInd-1);
                        dp[curInd-1] = dp[curInd]+1;
                    }
                }
    
                for (int nextInd : numToInd[arr[curInd]]) {
                    if (nextInd != curInd) {
                        if (dp[nextInd] == INT_MAX) {
                            frontier.push(nextInd);
                            dp[nextInd] = dp[curInd]+1;
                        }
                    }
                    if (nextInd == n-1) {
                        return dp[nextInd];
                    }
                }
                numToInd[arr[curInd]].clear();
            }
    
            return dp[n-1];
        }
    };
