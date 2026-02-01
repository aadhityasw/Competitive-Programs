// This is for the leetcode version of the problem


class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        int l = INT_MIN, r = 0;
        for (int w : weights) {
            l = max(l, w);
            r += w;
        }

        while (l < r) {
            int m = l + (r-l)/2;

            int curDays = 1;
            int curSum = 0;
            for (int w : weights) {
                if (w > m) {
                    curDays = INT_MAX;
                    break;
                }
                else if ((curSum+w) > m) {
                    curSum = w;
                    curDays++;
                }
                else {
                    curSum += w;
                }
                if (curDays > days) {
                    break;
                }
            }

            if (curDays <= days) {
                r = m;
            }
            else {
                l = m+1;
            }
        }

        return l;
    }
};
