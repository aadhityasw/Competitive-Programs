# Codechef
# Increasing Decreasing 
# https://www.codechef.com/problems/INCRDEC
# INCRDEC

"""
Chef received a new sequence A1,A2,…,AN. He does not like arbitrarily ordered sequences, so he wants to permute the elements of A in such a way that it would satisfy the following condition: there is an integer p (1≤p≤N) such that the first p elements of the new (permuted) sequence are strictly increasing and the last N−p+1 elements are strictly decreasing.

Help Chef and find a permutation of the given sequence which satisfies this condition or determine that no such permutation exists. If there are multiple solutions, you may find any one.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains N space-separated integers A1,A2,…,AN.
Output
For each test case:

If there is no permutation of A that satisfies the given condition, print a single line containing the string "NO" (without quotes).
Otherwise, print two lines.
The first of these lines should contain the string "YES" (without quotes).
The second line should contain N space-separated integers ― the elements of your permuted sequence.
Constraints
1≤T≤100
1≤N≤105
1≤Ai≤2⋅105 for each valid i
the sum of N over all test cases does not exceed 106
Subtasks
Subtask #1 (50 points):

N≤103
Ai≤2⋅103 for each valid i
the sum of N over all test cases does not exceed 104
Subtask #2 (50 points): original constraints

Example Input
5
4
1 3 2 4
4
1 3 2 4
6
1 10 10 10 20 15
5
1 1 2 2 3
4
1 2 3 3
Example Output
YES
1 2 3 4
YES
4 3 2 1
NO
YES
1 2 3 2 1
NO
"""

#%%

test = int(input())
for tes in range(test) :
    n = int(input())
    arr = list(map(int, input().strip().split()))
    freq = {}
    flag = True
    for num in arr :
        if num in freq :
            freq[num] += 1
            if freq[num] > 2 :
                flag = False
                break
        else :
            freq[num] = 1
    if freq[max(list(freq.keys()))] > 1 :
        flag = False
    if flag :
        print("YES")
        rem = []
        for num in sorted(list(freq.keys())) :
            print(num, end=" ")
            if freq[num] == 2 :
                rem.append(num)
        for num in reversed(sorted(rem)) :
            print(num, end=" ")
        print()
    else :
        print("NO")
