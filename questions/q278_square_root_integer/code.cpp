class Solution {
    public:
        int mySqrt(int x) {
            long s = 0, e =x;
            double m=0;
            while (s < e-1) {
                m = (s+e)/2;
                if (s == m) {
                    return s;
                }
                if (m*m == x) {
                    return floor(m);
                }
                else if (m*m < x) {
                    s = m;
                }
                else {
                    e = m;
                }
            }
            
            if (e*e == x) {
                return e;
            }
            return s;
        }
    };
