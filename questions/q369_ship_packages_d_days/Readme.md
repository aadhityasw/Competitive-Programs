# Capacity To Ship Packages Within D Days

https://practice.geeksforgeeks.org/problems/capacity-to-ship-packages-within-d-days/1



Given an array arr[] of N weights. Find the least weight capacity of a boat to ship all weights within D days.
Note: You have to load weights on the ship in the given order.

 

Example 1:

Input:
N = 3
arr[] = {1, 2, 1}
D = 2
Output:
3
Explanation:
We can ship the weights in 2 days
in the following way:-
Day 1- 1,2
Day 2- 1
Example 2:
Input:
N = 3
arr[] = {9, 8, 10}
D = 3
Output:
10
Explanation:
We can ship the weights in 3 days
in the following way:-
Day 1- 9
Day 2- 8
Day 3- 10
 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function leastWeightCapacity() which takes 2 integers N, and D, and an array arr of size N as input and returns the least weight capacity of the boat required.


Expected Time Complexity: O(N*log(Sum of weights - max(list of weights))
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N ≤ 10^5
1 ≤ arr[i] ≤ 100
1 ≤ D ≤ 5000
