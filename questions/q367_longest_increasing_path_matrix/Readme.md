# Longest Increasing Path in a Matrix


https://practice.geeksforgeeks.org/problems/longest-increasing-path-in-a-matrix/1



Given a matrix with n rows and m columns. Your task is to find the length of the longest increasing path in matrix, here increasing path means that the value in the specified path increases. For example if a path of length k has values a1, a2, a3, .... ak  , then for every i from [2,k] this condition must hold ai > ai-1.  No cell should be revisited in the path.
From each cell, you can either move in four directions: left, right, up, or down. You are not allowed to move diagonally or move outside the boundary.


Example 1:

Input:
n = 3, m = 3
matrix[][] = {{1 2 3},
              {4 5 6},
              {7 8 9}}
Output: 
5
Explanation: 
The longest increasing path is 
{1, 2, 3, 6, 9}. 
Example 2:

Input:
n = 3, m = 3
matrix[][] = {{3 4 5},
              {6 2 6},
              {2 2 1}}
Output: 
4
Explanation:
The longest increasing path is
{3, 4, 5, 6}.

Your Task:
You only need to implement the given function longestIncreasingPath() which takes the two integers n and m and the matrix matrix as input parameters, and returns the length of the longest increasing path in matrix.


Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)


Constraints:
1 ≤ n,m ≤ 1000
0 ≤ matrix[i] ≤ 2^30
