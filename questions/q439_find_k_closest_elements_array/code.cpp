class Solution {
    public:
        int findPos(int x, vector<int>& arr) {
            int low = 0, high = arr.size()-1, mid=low;
            while (low < high) {
                mid = (low+high)/2;
                if (arr[mid] == x) {
                    return mid;
                }
                else if (arr[mid] < x) {
                    low = mid;
                }
                else {
                    high = mid;
                }
                if (high == low+1) {
                    if (arr[high] == x) {
                        return high;
                    }
                    return low;
                }
            }
            return low;
        }
        
        vector<int> findClosestElements(vector<int>& arr, int k, int x) {
            
            int ind = findPos(x, arr);
            int start = ind, end=ind, n = arr.size();
            if (arr[ind] != x) {
                if (ind < n-1 && abs(arr[ind] - x) > abs(arr[ind+1] - x)) {
                    start++;end++;
                }
            }
            
            while (k > 1 && start>=0 && end<n) {
                if (start == 0 && end == n-1) {
                    break;
                }
                if (end >= n-1) {
                    start --;
                }
                else if (start == 0) {
                    end ++;
                }
                else {
                    if (abs(arr[start-1] - x) <= abs(arr[end+1] - x)) {
                        start--;
                    }
                    else {
                        end++;
                    }
                }
                k--;
            }
            
            vector<int> ans(arr.begin()+start, arr.begin()+end+1);
            return ans;
        }
    };
