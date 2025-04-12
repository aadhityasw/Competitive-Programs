class Solution {
    public:
    
    map<pair<int, int>, bool> dp;
  
  
      bool isSubsetSum(vector<int>& arr, int sum, int ind=0) {
          
          // Termination conditions
          if (sum < 0) {
              return false;
          }
          if (ind == arr.size()-1) {
              return sum == arr[ind] || sum == 0;
          }
  
          // Check in memory
          pair<int, int> key = {sum, ind};
          if (dp.find(key) != dp.end()) {
              return dp[key];
          }
  
          // Recursive step
          for (int i = ind+1; i<arr.size(); i++) {
              if (isSubsetSum(arr, sum-arr[ind], i) || isSubsetSum(arr, sum, i)) {
                  dp[key] = true;
                  return true;
              }
          }
  
          dp[key] = false;
          return false;
      }
  
  };
