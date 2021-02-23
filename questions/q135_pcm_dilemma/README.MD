# PCM Dilemma


https://www.codechef.com/CPAT002/problems/PCM


After mastering the art of Coding , Chef has decided to master Physics(P) , Chemistry(C) and Maths(M). Luckily he has three sisters where each sister is known to be master of exactly one subject. 
Now you are given a string of size 3 where character at index 1 denotes the subject known to sister I, character at index 2 denotes the subject known to sister II and character at index 3 denotes the subject known to sister III. You have to answer with either "YES" if chef can master "PCM" from his sisters or "NO" if he cannot.

Note
String will only contain characters from the set { P , C , M }.

Input
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
First and only line of each testcase contains the string mentioned.
Output
For each test case, output a single line containing either "YES" or "NO". 

Constraints
1 ≤ T ≤ 50
Length of string  = 3
Example
Input:
3
PCM
CCP
CPM

Output:
YES
NO
YES
Explanation 
For testcase 1 sister  I knows Physics(P) , sister II knows Chemistry(C) and sister III knows Maths(M) hence chef can master PCM.

Whereas in testcase II none of the sister knows Maths(M) hence answer is NO 
