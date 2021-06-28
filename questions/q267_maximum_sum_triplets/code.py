class Solution :
    def solve(self, A):
        n = len(A)
        right_max = [-1]*n
        maxi = A[-1]
 
        for i in reversed(range(n-1)):
            right_max[i] = maxi
            maxi = max(maxi, A[i])
            
        sk = []
        c = 0
        for i in range(n):
            if sk:
                while sk and sk[-1]>=right_max[i]:
                    sk.pop()
                while sk and sk[-1] < A[i] and A[i]<right_max[i]:
                    c = max(c , sk[-1] + A[i] + right_max[i])
                    sk.pop()
            sk.append(A[i])
        return c
