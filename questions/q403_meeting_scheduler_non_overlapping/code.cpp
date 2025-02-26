class Solution {
    public:
        vector<int> minAvailableDuration(vector<vector<int>>& slots1, vector<vector<int>>& slots2, int duration) {
            vector<int> ans;
            sort(slots1.begin(), slots1.end());
            sort(slots2.begin(), slots2.end());
    
            int ptr1=0, ptr2=0;
            int m = slots1.size();
            int n = slots2.size();
            int curStart, curEnd;
    
            while (ptr1 < m && ptr2 < n) {
                if (slots1[ptr1][1] < slots2[ptr2][0]) {
                    ptr1++;
                    continue;
                }
                else if (slots2[ptr2][1] < slots1[ptr1][0]) {
                    ptr2++;
                    continue;
                }
    
                curStart = max(slots1[ptr1][0], slots2[ptr2][0]);
                curEnd = min(slots1[ptr1][1], slots2[ptr2][1]);
                if (curEnd-curStart >= duration) {
                    ans.push_back(curStart);
                    ans.push_back(curStart+duration);
                    return ans;
                }
    
                if (slots1[ptr1][1] < slots2[ptr2][1]) {
                    ptr1++;
                }
                else {
                    ptr2++;
                }
            }
    
            return ans;
        }
};
