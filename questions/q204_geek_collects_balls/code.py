class Solution:
    def maxBalls(self, N, M, a, b):

        i = 0
        j = 0
        s1 = 0
        s2 = 0
        ans = 0

        while i < N and j < M :

            if a[i] == b[j] :
                while i < N-1 and a[i] == a[i+1] :
                    s1 += a[i]
                    i += 1
                while j < M-1 and b[j] == b[j+1] :
                    s2 += b[j]
                    j += 1
                ans += max(s1, s2) + a[i]
                i += 1
                j += 1
                s1 = 0
                s2 = 0
            elif a[i] < b[j] :
                s1 += a[i]
                i += 1
            elif b[j] < a[i] :
                s2 += b[j]
                j += 1

        if i < N :
            s1 += sum(a[i:])
        elif j < M :
            s2 += sum(b[j:])
        ans += max(s1, s2)

        return ans


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = [int(x) for x in input().split()]
        a = input().split()
        b = input().split()
        for i in range(N):
            a[i] = int(a[i])
        for i in range(M):
            b[i] = int(b[i])
        
        ob = Solution()
        print(ob.maxBalls(N, M, a, b))
