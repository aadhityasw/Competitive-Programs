#include <vector>

class Solution {
public:
    int candy(vector<int>& ratings) {
        vector<int> left(ratings.size());

        left[0] = 0;
        int i, sum=0, r=0;

        for (i=1; i < ratings.size(); i++) {
            if (ratings[i] > ratings[i-1]) {
                left[i] = left[i-1] + 1;
            }
            else {
                left[i] = 0;
            }
        }

        r = max(1, left[ratings.size()-1]+1);
        sum = r;

        for (i=ratings.size()-2; i>=0; i--) {
            if (ratings[i] > ratings[i+1]) {
                r += 1;
            }
            else {
                r = 1;
            }
            sum += max(r, left[i] + 1);
        }

        return sum;
    }
};