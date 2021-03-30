# Combination Sum

https://practice.geeksforgeeks.org/problems/combination-sum-part-21208/1


Given an array of integers A[] of size N and a sum B, find all unique combinations in A where the sum is equal to B. Each number in A may only be used once in the combination.

Note:
   All numbers will be positive integers.
   Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
   The combinations themselves must be sorted in ascending order.


Example 1:

Input: 
N = 7
A = {9, 1, 2, 7, 6, 1, 5}
B = 8
Output: (1 1 6)(1 2 5)(1 7)(2 6)
Explaination: These are the only possible 
combinations for getting sum 8.

Example 2:

Input:
N = 5
A = {8, 1, 8, 6, 8}
B = 12
Output: Empty
Explainatioin: We cannot obtain sum 12 
from the given elements.

Your Task:
You don't need to read input r print anything. Your task is to complete the function combinationSum() which takes the array A[], the length of the array N and the sum B as input parameters and returns all the combinations, otherwise, if there is no combination present it returns an empty list.


Expected Time Complexity: O(2N)
Expected Auxiliary Space: O(2N)


Constraints:
0 < N < 13
0 <= A[i] <= 9
0 < B <= 30
