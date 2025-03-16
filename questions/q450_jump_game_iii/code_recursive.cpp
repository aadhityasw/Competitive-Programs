class Solution {
    public:
        map<int, bool> indexToResult;
    
        bool search(vector<int>& arr, int start, set<int>& curPath) {
            if (indexToResult.find(start) != indexToResult.end()) {
                return indexToResult[start];
            }
    
            if (arr[start] == 0) {
                indexToResult[start] = true;
                return true;
            }
    
            if (curPath.count(start) > 0) {
                return false;
            }
    
            curPath.insert(start);
            bool canReachEndRight = (start+arr[start] < arr.size()) ? search(arr, start+arr[start], curPath) : false;
            bool canReachEndLeft = (start-arr[start] >= 0) ? search(arr, start-arr[start], curPath) : false;
            curPath.erase(start);
    
            indexToResult[start] = canReachEndRight || canReachEndLeft;
            return indexToResult[start];
        }
    
        bool canReach(vector<int>& arr, int start) {
            set<int> curPath;
            return search(arr, start, curPath);
        }
    };
