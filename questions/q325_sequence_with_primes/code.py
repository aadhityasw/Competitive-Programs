class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return a list of integers
    def solve(self, A, B, C, D):

        i, j, k = 0, 0, 0
        p1, p2, p3 = A, B, C

        ans = []
        while len(ans) < D :
            min_val = min(p1, p2, p3)
            ans.append(min_val)

            if min_val == p1 :
                p1 = A * ans[i]
                i += 1
            if min_val == p2 :
                p2 = B * ans[j]
                j += 1
            if min_val == p3 :
                p3 = C * ans[k]
                k += 1
        
        return ans
