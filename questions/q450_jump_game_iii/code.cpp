class Solution {
    public:
        bool canReach(vector<int>& arr, int start) {
            int n = arr.size();
            queue<int> frontier;
            frontier.push(start);
            vector<int> visited(n, false);
    
            while (frontier.size() > 0) {
                int curInd = frontier.front();
                frontier.pop();
                if (arr[curInd] == 0) {
                    return true;
                }
                if(curInd+arr[curInd] < n && !visited[curInd+arr[curInd]]) {
                    frontier.push(curInd+arr[curInd]);
                }
                if(curInd-arr[curInd] >= 0 && !visited[curInd-arr[curInd]]) {
                    frontier.push(curInd-arr[curInd]);
                }
                visited[curInd] = true;
            }
    
            return false;
        }
    };
