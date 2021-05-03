# Special Matrix


https://practice.geeksforgeeks.org/contest/interview-series-google/problems/


Given N and a square matrix with dimensions NxN. Find the minimum number of moves required to make a matrix special. In a single move, you can select an arbitary element and increase/decrease it by 1.

A special matrix is defined as a matrix where at least one row or column that contains only special numbers.

A special number P is a non-negative integer for which the following quadratic equation has at least one negative integer root:

x2-(2*P)+x=0
 


Example 1:

Input:
N = 3
matrix[] = {(1, 2, 3), (4, 5, 6), (7, 8, 9)}
Output: 1
Explanation:
Increasing the second element in first
row will make it (1, 3, 3)
Example 2:

Input:
N = 2
arr[] = {(1,2), (1,3)}
Output: 0
Explanation:
First column is already special.

Your Task:  
You don't need to read input or print anything. Your task is to complete the function minMoves() which takes the integer N, and the matrix as input parameters and returns the minimum number of moves required.


Expected Time Complexity: O(N*N)
Expected Auxiliary Space: O(constant)


Constraints:
1 ≤ N ≤ 500
1 ≤ matrix[i][j] ≤ 1011
