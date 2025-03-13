class Solution {
    public:
        int minMeetingRooms(vector<vector<int>>& intervals) {
            priority_queue<int, vector<int>, greater<int>> confRooms;
            int n = intervals.size();
            int numConfRooms = 1;
            int ans = 1;
    
            sort(intervals.begin(), intervals.end());
            confRooms.push(intervals[0][1]);
    
            int i=1;
            while (i < n) {
                if (confRooms.size() == 0 || intervals[i][0] < confRooms.top()) {
                    numConfRooms++;
                    ans = max(ans, numConfRooms);
                    confRooms.push(intervals[i][1]);
                }
                else {
                    confRooms.pop();
                    confRooms.push(intervals[i][1]);
                }
                i++;
            }
    
            return ans;
        }
    };
