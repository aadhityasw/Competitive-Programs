class Solution {
    public:
    
        vector<vector<int>> splitAndAccumulateSum (vector<int> &nums, int s, int e) {
            int n = e - s + 1;
    
            // Create a vector to store the sums, where ith position has the sum of all combinations of i choosen numbers
            vector<vector<int>> sums(n+1);
    
            // There are 2^n subsets possible, we will enumerate their sums
            for (int ind=0; ind<pow(2, n); ind++) {
                // Count the number of entries whose sum is being found here
                int curCount = 0;
                int curSum = 0;
    
                for (int j=0; j<n;j++) {
                    // If the jth bit is set, then we include the jth number into the sum
                    if (ind & 1<<j) {
                        curSum += nums[s + j];
                        curCount++;
                    }
                }
    
                // Add the found sum to the appropriate vector
                sums[curCount].push_back(curSum);
            }
    
            for (int i=0; i<n+1; i++) {
                sort(sums[i].begin(), sums[i].end());
            }
    
            return sums;
        }
    
        int minimumDifference(vector<int>& nums) {
            int n2 = nums.size();
            int n = n2/2;
            int totalSum = 0;
    
            // Find the total sum of all elements
            for (int num : nums) {
                totalSum += num;
            }
            
            // Split the array into 2 halves for meet in the middle
            vector<vector<int>> left = splitAndAccumulateSum(nums, 0, n-1);
            vector<vector<int>> right = splitAndAccumulateSum(nums, n, n2-1);
    
            // Take the sums with 0 element from left and n elements from right and compare, and so on for all combinations
            int minDiff = INT_MAX;
            for (int i=0; i<=n; i++) {
                for (int j=0; j<left[i].size(); j++) {
                    int s = 0;
                    int e = right[n-i].size()-1;
    
                    // Compute the element to find
                    // We need to minimize (2*(lSum + rSum) - tSum)
                    // We have lSum, and need to figure out the best rSum
                    int rSum = (totalSum/2) - left[i][j];
    
                    while (s < e) {
                        int mid = s + (e-s)/2;
    
                        if (right[n-i][mid] > rSum) {
                            e = mid;
                        }
                        else {
                            s = mid+1;
                        }
                    }
    
                    minDiff = min(
                        minDiff,
                        abs(totalSum - 2*(left[i][j] + right[n-i][s]))
                    );
    
                    // Just for safety check the next and previous element too if needed
                    if (s > 0) {
                        minDiff = min(
                            minDiff,
                            abs(totalSum - 2*(left[i][j] + right[n-i][s-1]))
                        );
                    }
                    if (s < right[n-i].size()-1) {
                        minDiff = min(
                            minDiff,
                            abs(totalSum - 2*(left[i][j] + right[n-i][s+1]))
                        );
                    }
                }
            }
    
            return minDiff;
        }
    };
