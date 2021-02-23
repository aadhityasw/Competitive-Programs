# We subtract the total length of the input word from the length of the longest palindrome subsequence.


def longestPalindromeSubsequence(s) :
    w = ''.join(reversed(s))
    n = len(s)
    a = [[0 for _ in range(n+1)] for _ in range(n+1) ]
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            if s[i-1] == w[j-1] :
                a[i][j] = 1 + a[i-1][j-1]
            else :
                a[i][j] = max(a[i-1][j], a[i][j-1])
    return a[n][n]


T = int(input())

for tes in range(T) :
    s = input().strip()    
    print(len(s) - longestPalindromeSubsequence(s))
