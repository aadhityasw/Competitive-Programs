
class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        table = [[0 for _ in range(m+1)] for _ in range(n+1)]

        max_len = 0
        for i in range(1, n+1) :
            for j in range(1, m+1) :
                if S1[i-1] == S2[j-1] :
                    table[i][j] = 1 + table[i-1][j-1]
                    max_len = max(max_len, table[i][j])
        
        return max_len


if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
