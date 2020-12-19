# Square arrays



You are given an Array of integers A1, A2......AN. You are required to perform 2 types of queries in the array :

1 x y. Add 1x2 to Ax, add 2x3 to Ax+1, add 3x4 to Ax+2, add 4x5 to Ax+3, And so on until Ay.

2 x y. Find the sum of all integers from index x to index y modulo 109. In other words determine (Ax + Ax+1 + ... + Ay) mod (109). You can assume that initially, all the values in the array are 0.

Input Format

The first line contains two space-separated integers N and Q. Here, N denotes the size of the array and Q denotes the number of queries.
Each of the next Q lines contains a query of the form 1 x y or 2 x y.
Constraints

For each query of the form 2 x y, print the required answer.

Output Format

1 <= x <= y <= N
1 <= N <= 2 <= 105
1 <= Q <= 2 <= 105
Sample Input 0

10 5
1 1 10
2 2 7
1 4 8
1 5 6
2 6 6
Sample Output 0

57
60
Explanation 0

After the first query, the array is [2,6,12,20,30,42,56,72,90,110]. The answer for the second query is 6+12+20+30+42+56=166, 166mod109=57, after the third query, the array is [2,6,12,22,36,54,76,102,90,110]. The answer for the fifth query is 60, 60mod109=60.
