# Happiest Class


https://www.codechef.com/MISC2021/problems/MCQ4


There are n children in a class. Each child has a favorite color. The favorite color of the i-th child is fi. As a gift for their promotion to the next class, you plan to give each child k candies as a gift. So, you bring n*k candies to the class and plan to distribute them. 

Each candy has a single, non-distinct color, i.e., there may be more than one candy with the same color. When a child receives j candies of his/her favorite color, the happiness level of a child becomes hj. Any other color of candy adds no happiness to the child.
As a good and unbiased teacher, you want to make the entire class as happy as possible. The happiness of the whole class is defined as the sum of happiness of each child. Given the n, k, f, and h, find the highest possible happiness level of the class.

Input Format
The first line contains two integers, n (1 ≤ n ≤ 500), the number of children and k (1 ≤k ≤ 50), the number of candies each child will get.
The second line contains `k * n` integers c1, c2, …, ck*n (1 ≤ ci ≤ 10^5) which are the index of colours.
The third line contains n integers f1, f2, …, fn (1 ≤ fi ≤ 10^5) where fi is the favourite colour of the i-th child.
The fourth line contains k integers h1, h2, …, hk (1 ≤ hi ≤ 10^5) where hi is the happiness level of the child on receiving i candies of favourite colour.
It is guaranteed that hi > hi−1 for i ∈ [2..k]. So, more favourite candies = more happiness.

Output Format
A single integer displaying the maximum possible happiness of the class.

Time Limit:	5 secs

Sample Test :
Sample IO
Input:
6 3
9 4 1 1 3 2 8 5 5 8 2 2 8 5 2 7 1 2
1 2 2 5 9 7
3 6 8

Output:
36

Explanation:
Student 1 gets [1,1,1] => 8 happiness.
Student 2 gets [2,2,2] => 8 happiness.
Student 3 gets [8,2,2] => 6 happiness.
Student 4 gets [5,5,5] => 8 happiness.
Student 5 gets [3,9,4] => 3 happiness.
Student 6 gets [8,7,8] => 3 happiness.
