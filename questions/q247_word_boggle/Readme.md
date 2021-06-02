# Word Boggle


https://practice.geeksforgeeks.org/problems/word-boggle4143/1


Given a dictionary of distinct words and an M x N board where every cell has one character. Find all possible words from the dictionary that can be formed by a sequence of adjacent characters on the board. We can move to any of 8 adjacent characters, but a word should not have multiple instances of the same cell.


Example 1:

Input: 
N = 1
dictionary = {"CAT"}
R = 3, C = 3
board = {{C,A,P},{A,N,D},{T,I,E}}
Output:
CAT
Explanation: 
C A P
A N D
T I E
Words we got is denoted using same color.
Example 2:

Input:
N = 4
dictionary = {"GEEKS","FOR","QUIZ","GO"}
R = 3, C = 3 
board = {{G,I,Z},{U,E,K},{Q,S,E}}
Output:
GEEKS QUIZ
Explanation: 
G I Z
U E K
Q S E 
Words we got is denoted using same color.

Your task:
You don’t need to read input or print anything. Your task is to complete the function wordBoggle() which takes the dictionary contaning N space-separated strings and R*C board as input parameters and returns a list of words that exist on the board.


Expected Time Complexity: O(N*W + R*C^2)
Expected Auxiliary Space: O(N*W + R*C)


Constraints:
1 ≤ N ≤ 15
1 ≤ R, C ≤ 50
1 ≤ length of Word ≤ 60
