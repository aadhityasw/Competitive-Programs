class Solution {
    public:
        int maxFreeTime(int eventTime, int k, vector<int>& startTime, vector<int>& endTime) {
            vector<int> freeTimes;
    
            int prevEndTime = 0;
            for (int i=0; i<startTime.size(); i++) {
                freeTimes.push_back(startTime[i] - prevEndTime);
                prevEndTime = endTime[i];
            }
            if (prevEndTime < eventTime) {
                freeTimes.push_back(eventTime-prevEndTime);
            }
    
            // Find the max sum k concecutive numbers in this array
            int n = freeTimes.size();
            int curWinSize=0, start=0,end=0;
            int maxSum=0,curSum=0;
    
            while (end < n) {
                curSum += freeTimes[end];
                if (curSum > maxSum) {
                    maxSum = curSum;
                }
                end++;
    
                while (end-start > k) {
                    curSum -= freeTimes[start];
                    start++;
                }
                
            }
    
            return maxSum;
        }
    };
