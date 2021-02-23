# Students, heights and their IQs

* HEIGHTIQ

* https://www.codechef.com/CPAT002/problems/HEIGHTIQ


In the school morning assembly, n
 students standing in a line. You, being the principal of the school know the heights and IQ levels of the students. This information is provided to you by an array h
 and iq
, where hi,iqi
 denotes the height and the IQ of the i
-th student, respectively.

You want to find the longest subsequence of the students such that their heights are in strictly increasing order, whereas their IQ levels in strictly decreasing order. Note that a subsequence is gotten by removing some (possibly zero) students from the line.

Find out the length of longest such subsequence.

Input
The first line of the input contains a single integer T
 denoting the number of test cases. The description of T
 test cases follows.
The first line of each test case contains an integer n
.
The second line contains n
 space-separated integers h1,h2,…,hn
.
The third line contains n
 space-separated integers iq1,iq2,…,iqn
.
Output
For each test case, print a single line containing one integer — the answer to the problem.

Constraints
1≤T≤5
1≤n≤103
1≤hi,iqi≤109
Subtasks
For 30% of the score: 1≤n≤15
Remaining 70%: No extra constraints.
Sample Input
2
3
1 2 3
3 2 1
4
1 3 2 4
5 6 4 4
Sample Output
3
2
Explanation
Example case 1: You can choose the subsequence {1, 2, 3} of the students. You can see the heights of the students are increasing from left to right, whereas the IQ levels are decreasing.

Example case 2: You can choose the subsequence {2, 4} of the students. You can see the height of 4-th student is 4, which is greater than the height of 2-nd student (3). The IQ levels of 4-th student (4) is less than the 2nd student (6). Hence, the answer is 2.

