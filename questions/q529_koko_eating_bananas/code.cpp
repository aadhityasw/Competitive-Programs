class Solution {
public:
    int calcHoursToEat(vector<int>& piles, int curSpeed) {
        int time = 0;
        for (int ban : piles) {
            time += (floor((double)ban/curSpeed)) + ((ban%curSpeed==0)? 0 : 1);
        }
        return time;
    }

    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1, r = piles[0];
        for (int ban : piles) {
            r = max(r, ban);
        }

        while (l < r) {
            int m = l + (r-l)/2;

            int curTime = calcHoursToEat(piles, m);
            if (curTime <= h) {
                r = m;
            }
            else {
                l = m+1;
            }
        }

        return l;
    }
};
