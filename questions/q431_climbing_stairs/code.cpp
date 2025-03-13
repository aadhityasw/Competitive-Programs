class Solution {
    public:
        double choose (int n, int k) {
            double ans = 1;
            for (int i=n;i>n-k;i--) {
                ans *= i;
            }
            for (int i=k; i>0; i--) {
                ans = ans/i;
            }
            return ans;
        }
    
        int climbStairs(int n) {
            int num1 = n%2;
            int num2 = (n/2);
            double count=0;
    
            while (num2 >= 0) {
                count += choose(num1+num2, num2);
                num2--;
                num1+=2;
            }
    
            return (int)count;
        }
    };
