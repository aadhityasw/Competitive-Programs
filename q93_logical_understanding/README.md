# Logical Understanding


You have a dollar of value N. We can exchange this note for three notes of value (N/2,N/3,N/4) each. Then we can exchange these notes directly with 1:1 exchange rate with European pound. Your intention is to make the maximum possible amount in European pounds.

Input Format

Integer : N

Constraints

N < 100

Output Format

Integer

Sample Input 0

50
Sample Output 0

57
Explanation 0

First split: N = 50; (50/2)=25 ; (50/3)=16 ; (50/4)=12; (25 +16+12)= 53;
Second split: N=25; (25/2)=12 ; (25/3)=8; (25/4)=6; (12+8+6)= 26; N=16; (16/2)=8; (16/3)=5; (16/4)=4; (8+5+4)=17; N=12; (12/2)=6;(12/3)=4;(12/4)=3; (6+4+3)=13; 26 + 17 + 13 = 56;
From above split only 12 from N=25(from second split) can be more split to 13 hence last split is 13 + 8 + 6 + 8 + 5 + 4 + 6 + 4 + 3 = 57. Similarly keep on exchanging to get maximum profit.
