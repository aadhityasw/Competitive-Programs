// This approach is based on the idea that we can distribute candies in increasing order and then in decreasing order.
// We calculate the count of increasing and decreasing sequence and then calculate the sum of candies required for each sequence.

// Not the best approach but it works, there are still some edge cases that are not handled in this approach, but this passes the leetcode problem.



class Solution {
public:
    int candy(vector<int>& ratings) {
        if (ratings.size() == 1) {
            return 1;
        }

        int sum=0, i=1, inc_count=0, dec_count=0, eq_count = 0;

        while (i < ratings.size()) {
            inc_count = 0;
            while ((i < ratings.size()) && (ratings[i] > ratings[i-1])) {
                inc_count ++;
                i++;
            }
            if (inc_count > 0) {
                if (dec_count == 0) {
                    sum += (inc_count * (inc_count + 1))/2;
                }
                else {
                    sum += (inc_count * (inc_count + 1))/2 - 1;
                }
            }
            inc_count ++;
            
            eq_count = 0;
            while ((i < ratings.size()) && (ratings[i] == ratings[i-1])) {
                eq_count ++;
                i++;
            }
            if (eq_count > 0 && inc_count > 1) {
                sum += inc_count;
                inc_count = 1;
            }
            if (eq_count == i-1) {
                eq_count++;
            }
            

            dec_count = 0;
            while ((i < ratings.size()) && (ratings[i] < ratings[i-1])) {
                dec_count ++;
                i++;
            }
            sum += (dec_count * (dec_count + 1))/2;

            if (dec_count > 0) {
                dec_count++;
                if (inc_count > dec_count) {
                    sum += inc_count;
                }
                else {
                    sum += dec_count;
                }

                if (eq_count > 0) {
                    sum += (eq_count-1);
                    eq_count = 0;
                }
                inc_count = 0;
            }
            else if (eq_count > 0) {
                inc_count = 0;
                dec_count++;
            }
            
            sum += eq_count + inc_count;
        }

        return sum;
    }
};