# Minimum indexed character

https://practice.geeksforgeeks.org/problems/minimum-indexed-character-1587115620/1#


Given a string str and another string patt. Find the character in patt that is present at the minimum index in str. If no character of patt is present in str then print ‘No character present’.

Example 1:

Input:
str = geeksforgeeks
patt = set
Output: e
Explanation: e is the character which is
present in given patt "geeksforgeeks"
and is first found in str "set".
Example 2:

Input:
str = adcffaet
patt = onkl
Output: No character present
Explanation: There are none of the
characters which is common in patt
and str.
Your Task:
You only need to complete the function minIndexChar() that returns the index of answer in str or returns -1 in case no character of patt is present in str.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Number of distinct characters).

Constraints:
1 <= |str|,|patt| <= 10^5
