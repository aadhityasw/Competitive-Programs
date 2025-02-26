class Solution {
    public:
        int maxFreeTime(int eventTime, vector<int>& startTime, vector<int>& endTime) {
            int n = startTime.size();
            vector<int> freeTime;
            vector<int> meetTime;
    
            int prevEndTime = 0;
            for(int i=0; i<n; i++) {
                freeTime.push_back(startTime[i]-prevEndTime);
                prevEndTime = endTime[i];
                meetTime.push_back(endTime[i] - startTime[i]);
            }
            freeTime.push_back(eventTime-prevEndTime);
    
            vector<int> leftMax(freeTime.size());
            vector<int> rightMax(freeTime.size());
    
            int curMax = 0;
            for (int i=0; i<freeTime.size(); i++) {
                leftMax[i] = curMax;
                curMax = max(curMax, freeTime[i]);
            }
            curMax = 0;
            for (int i=freeTime.size()-1; i>=0; i--) {
                rightMax[i] = curMax;
                curMax = max(curMax, freeTime[i]);
            }
    
            int ans=0;
            for (int i=0; i<meetTime.size(); i++) {
                int curWin = freeTime[i] + freeTime[i+1] + meetTime[i];
                if (leftMax[i] >= meetTime[i] || rightMax[i+1] >= meetTime[i]) {
                    ans = max(ans, curWin);
                }
                else {
                    int neigMax = max(freeTime[i], freeTime[i+1]);
                    int neigMin = min(freeTime[i], freeTime[i+1]);
    
                    if (neigMax >= meetTime[i] || neigMax > 0) {
                        ans = max(ans, neigMin+neigMax);
                    }
                }
            }
    
            return ans;
        }
    };
