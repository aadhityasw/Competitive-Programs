#include<string>
class Solution {
public:
    string intToRoman(int num) {
        char romans[7] = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};

        int divisor=1000, i=6, d;
        string ans = "";

        if (num > 3999) {
            return "Issue";
        }

        while (i >= 0) {
            d = num / divisor;

            if (d > 0 && d < 4) {
                for (int j=0;j<d;j++)
                    ans += romans[i];
            }
            else if (d == 4) {
                ans += romans[i];
                ans += romans[i+1];
            }
            else if (d == 5) {
                ans += romans[i+1];
            }
            else if (d > 5 and d < 9) {
                ans += romans[i+1];
                for (int j=0;j<d-5;j++)
                    ans += romans[i];
            }
            else if (d == 9) {
                ans += romans[i];
                ans += romans[i+2];
            }

            i -= 2;
            num = num % divisor;
            divisor = divisor / 10;
        }

        return ans;
    }
};