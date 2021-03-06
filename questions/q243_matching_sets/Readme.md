# Maching Sets

https://www.codechef.com/MISC2021/problems/MCQ7


Bob gave Anna a sequence of Q integers: K1, K2, K3,…Kn. She is asked to find the Number of sets (i,j) such a way Ki | Kj ≤ max(Ki, Kj) and 1≤ i < j ≤ Q.
Can you help Anna with the problem?

Input
The first line of the input contains an integer T, denoting the number of test cases. The description of each testcase follows.
The first line of each testcase contains a single integer: Q
The second line of each testcase contains Q integers: K1,K2,K3,..Kn.

Output
For each test case, output a single line containing the answer for that test case.

Constraints
1 ≤ T ≤ 50
1 ≤ Q ≤ 106
0 ≤ Ki ≤ 106
1 ≤ Sum of Q over all test cases ≤ 106

Example Input
1
3
1 2 3

Output:
2

Explanation:
There are three possible pairs of indices which satisfy 1 ≤ i < j ≤ Q: (1, 2), (1, 3) and (2, 3). Let us see which of those satisfy Ki | Kj ≤ max(Ki, Kj):
• (1, 2): K1 | K2 = 1 | 2 = (01) 2 | (10) 2 = (11) 2 = 3. But max(K1, K2) = max(1, 2) = 2, and 3 ≤ 2 is not correct. Hence this is not a valid pair.
• (1, 3): K1 | K3 = 1 | 3 = (01) 2 | (11) 2 = (11) 2 = 3. And max(K1, K3) = max(1, 3) = 3, and 3 ≤ 3 is correct. Hence this is a valid pair.
• (2, 3): K2 | K3 = 2 | 3 = (10) 2 | (11) 2 = (11) 2 = 3. And max(K2, K3) = max(2, 3) = 3, and 3 ≤ 3 is correct. Hence this is a valid pair.
So there are a total of 2 valid pairs, and hence the answer is 2.
