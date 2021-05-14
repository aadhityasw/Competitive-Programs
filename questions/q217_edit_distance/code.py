class Solution:
    def editDistance(self, s, t):
        table = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]

        for i in range(len(s)+1) :
            table[i][0] = i
        for i in range(len(t)+1) :
            table[0][i] = i

        for i in range(1, len(s)+1) :
            for j in range(1, len(t)+1) :
                table[i][j] = min(
                    table[i-1][j] + 1,
                    table[i][j-1] + 1,
                    table[i-1][j-1] + (0 if s[i-1] == t[j-1] else 1) # 0 if charater is equal else 1
                )
            
        return table[len(s)][len(t)]



if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        s, t = input().split()
        ob = Solution();
        ans = ob.editDistance(s, t)
        print(ans)
