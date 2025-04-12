#include <bits/stdc++.h>
using namespace std;


class Solution {
    public:
      int maximumPoints(vector<vector<int>>& arr) {
          vector<vector<int>> dp(arr.size(), vector<int>(arr[0].size()));
          int m = arr.size(), n = arr[0].size();
          
          for (int i=0; i<n; i++) {
              dp[0][i] = arr[0][i];
          }
          
          for (int i=1; i<m; i++) {
              for (int j=0; j<n; j++) {
                  int maxEle = INT_MIN;
                  for (int k=0; k<n; k++) {
                      if (k != j) {
                          maxEle = max(maxEle, dp[i-1][k]);
                      }
                      dp[i][j] = maxEle + arr[i][j];
                  }
              }
          }
          
          int maxEle = INT_MIN;
          for (int i=0; i<n; i++) {
              maxEle = max(maxEle, dp[m-1][i]);
          }
          
          return maxEle;
      }
  };

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<vector<int>> arr;
        for (int i = 0; i < n; ++i) {
            vector<int> temp;
            for (int j = 0; j < 3; ++j) {
                int x;
                cin >> x;
                temp.push_back(x);
            }
            arr.push_back(temp);
        }

        Solution obj;
        cout << obj.maximumPoints(arr) << endl;
        cout << "~" << endl;
    }
    return 0;
}
