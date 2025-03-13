class Solution {
    public:
        vector<vector<int>> merge(vector<vector<int>>& intervals) {
            sort(intervals.begin(), intervals.end());
    
            int n = intervals.size(),i=0;
            vector<vector<int>> ans;
            int s = 0, e=0;
            while (i<n) {
                if (i < n && intervals[i][0] <= intervals[e][1]) {
                    if (intervals[e][1] < intervals[i][1]) {
                        e = i;
                    }
                }
                else {
                    ans.push_back({intervals[s][0], intervals[e][1]});
                    e = i;
                    s = i;
                }
                i++;
            }
            ans.push_back({intervals[s][0], intervals[e][1]});
    
            return ans;
        }
    };
