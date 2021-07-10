# Minimum Integer Points Required for Path Traversal

Given a grid with each cell consisting of positive, negative or no points i.e, zero points. We can move across a cell only if we have positive points ( > 0 ). Whenever we pass through a cell, points in that cell are added to our overall points. We need to find minimum initial points to reach cell (m-1, n-1) from (0, 0) by following these certain set of rules :



1.From a cell (i, j) we can move to (i+1, j) or (i, j+1).

2.We cannot move from (i, j) if your overall points at (i, j) are <= 0.

3.We have to reach (n-1, m-1) with minimum positive points i.e., > 0.



Example:

Input: points[m][n] = { {-2, -3,  3}, 

                       {-5, -10, 1}, 

                       {10, 30, -5} 

                     };

Output: 7

Explanation: 

7 is the minimum value to reach destination with 

positive throughout the path. Below is the path.



(0,0) -> (0,1) -> (0,2) -> (1, 2) -> (2, 2)



We start from (0, 0) with 7, we reach(0, 1) 

with 5, (0, 2) with 2, (1, 2) with 5, (2, 2)

with and finally we have 1 point (we needed 

greater than 0 points at the end).



Input format
The input contains two integers 'R' and 'C' denoting the number of rows and column of an array. It is followed by the space-separated values of the array i.e the grid, in a single line separated by spaces in row-major order.

Output format
Print the minimum initial points to reach the bottom rightmost cell in a separate line.

Code constraints
1 ≤ R,C ≤ 10

-30 ≤ A[R][C] ≤ 30

Sample testcases
Input 1
3 3 -2 -3 3 -5 -10 1 10 30 -5
Output 1
7
