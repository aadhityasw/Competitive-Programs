class Solution:
    

    def longestCommonSubstr(self, S1, S2, n, m):
        table = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(1, n+1) :
            for j in range(1, m+1) :
                if S1[i-1] == S2[j-1] :
                    table[i][j] = 1 + table[i-1][j-1]
                else :
                    table[i][j] = max(table[i-1][j], table[i][j-1])
        
        return table[n][m]
    

    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, X, Y, m, n):
        lcs = self.longestCommonSubstr(X, Y, m, n)
        return m + n - lcs


if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        X,Y=input().split()
        
        print(Solution().shortestCommonSupersequence(X,Y,len(X),len(Y)))
 