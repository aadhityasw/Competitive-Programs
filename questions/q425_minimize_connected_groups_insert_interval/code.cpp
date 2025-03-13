class Solution {
    public:
        int minConnectedGroups(vector<vector<int>>& intervals, int k) {
            sort(intervals.begin(), intervals.end());
    
            int n = intervals.size(), s=0, e=0, i=0;
            vector<vector<int>> mergedInterval;
            //vector<int> intervalGaps;
            int lastIntervalEnd=-1;
            while (i < n) {
                if (intervals[e][1] >= intervals[i][0]) {
                    if (intervals[e][1] <= intervals[i][1]) {
                        e = i;
                    }
                }
                else {
                    mergedInterval.push_back({intervals[s][0], intervals[e][1]});
                    /*if (lastIntervalEnd >= 0) {
                        intervalGaps.push_back(intervals[s][0] - lastIntervalEnd);
                    }*/
                    lastIntervalEnd = intervals[e][1];
                    s=i;e=i;
                }
                i++;
            }
            mergedInterval.push_back({intervals[s][0], intervals[e][1]});
            /*if (lastIntervalEnd >= 0) {
                intervalGaps.push_back(intervals[s][0] - lastIntervalEnd);
            }*/
            
    
            s=0;e=1;n=mergedInterval.size();
            int curSum=0;
            int maxCount=1;
            while (e<n) {
                curSum = (mergedInterval[e][0] - mergedInterval[s][1]);
                if (curSum <= k) {
                    if (curSum >= 0) {
                        maxCount = max(maxCount, e-s+1);
                    }
                    e++;
                }
                else {
                    s++;
                }
            }
    
            return n+1-maxCount;
        }
    };
