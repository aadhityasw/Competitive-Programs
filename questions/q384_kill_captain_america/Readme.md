# Kill Captain America



https://practice.geeksforgeeks.org/problems/kill-captain-america0228/1/



Captain America is hiding from Thanos in a maze full of rooms.
The maze is designed in such a way that the room, within it, leads to another room via gate. Captain America is hiding only in those rooms which are accessible directly/indirectly through every other room in the maze.
Further provided that, the movement from one room (R1) to another room (R2) is one way(unidirectional) only .
Now, you being on Thanos side, want to kill Captain America.  

 

Example 1:

Input:
N = 5 and M =5
V = [[1, 2], [2, 3], [3, 4], [4, 3], [5, 4]]
Output: 2
Explanation:
We can look closesly after forming graph 
than captain america only can hide in a 
room 3 and 4 because they are the only room 
which have gates through them. So,
answer is 2.

Example 2:

Input:
N = 2, M = 1
V = [[1, 2]]
Output: 1

Your Task:  
You don't need to read input or print anything. Your task is to complete the function captainAmerica() which takes the integer N, an integer M and 2-d array V as input parameters and returns the Total no of rooms.

Expected Time Complexity: O(N+M)
Expected Auxiliary Space: O(N+M)

 

Constraints:
1 ≤ n ≤ 30000
1 ≤ m ≤ 200000
1 ≤ p,q ≤ n
