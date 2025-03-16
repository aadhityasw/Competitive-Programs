// This is a little less optimized than the direct version,
// This keeps squaring till we cross the value and then keep dividing till we reach value of n in x^n
// log(n) till squaring, but o(n) while dividing back so little less optimized


class Solution {
    public:
        double myPow(double x, long n) {
            if (x == 1) {
                return x;
            }
            if (n == 0) {
                return 1;
            }
            else if (n < 0) {
                return myPow((double)(1/x), (-1*n));
            }
            
            double i=1;
            double p = x;
            while (i<n) {
                p = p*p;
                i*= 2;
                while (i > n) {
                    p = p / x;
                    i--;
                }
            }
            
            return p;
        }
    };
